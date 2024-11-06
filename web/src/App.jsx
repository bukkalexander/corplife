import React, { useState, useEffect } from 'react';
import { Amplify } from 'aws-amplify';
import { signIn, signUp, signOut, resendSignUpCode, confirmSignUp, getCurrentUser } from '@aws-amplify/auth';
import ResultBoard from './ResultBoard.jsx';
import QuestionBoard from './QuestionBoard.jsx';
import Login from './Login.jsx';

const CONFIG_URL = "./config.json";

const fetchConfig = async (config_url) => {
  try {
    console.log("Fetching config...")
    const response = await fetch(config_url);
    console.log("Fetching config DONE")
    if (!response.ok) {
      throw new Error(`Failed to fetch config: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching config:', error);
    return null;
  }
};

const fetchQuestions = async (api_url) => {

  const fetchQuestionsUrl = `${api_url}/questions` ;
  console.log(fetchQuestionsUrl)
  try {
    console.log("Fetching questions...")
    const response = await fetch(fetchQuestionsUrl);

    console.log("Fetching questions DONE")
    if (!response.ok) {
      throw new Error(`Failed to fetch: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching questions:', error);
    return [];
  }
};

function App() {
  const [config, setConfig] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [isFetchingQuestions, setIsFetchingQuestions] = useState(true);
  const [user, setUser] = useState(null);
  const [cognitoConfigured, setCognitoConfigured] = useState(false);


  useEffect(() => {
    const loadConfig = async () => {
      const fetchedConfig = await fetchConfig(CONFIG_URL);
      console.log(fetchedConfig)
      setConfig(fetchedConfig);
    };
    console.log("Loading config...")
    loadConfig();
    console.log("Loading config DONE")

  }, []);

  // Initialize Amplify after `config` is set
  useEffect(() => {
      if (config) {
        Amplify.configure({
          Auth: {
            Cognito: {
              userPoolId: config.userPoolId,
              userPoolClientId: config.userPoolWebClientId,
              allowGuestAccess: true,
              //OPTIONAL - This is used when autoSignIn is enabled for Auth.signUp
              // 'code' is used for Auth.confirmSignUp, 'link' is used for email link verification
              //signUpVerificationMethod: 'code', // 'code' | 'link'
              /*
              loginWith: {
                // OPTIONAL - Hosted UI configuration
                oauth: {
                  domain: 'your_cognito_domain',
                  scopes: [
                    'phone',
                    'email',
                    'profile',
                    'openid',
                    'aws.cognito.signin.user.admin'
                  ],
                  redirectSignIn: ['http://localhost:3000/'],
                  redirectSignOut: ['http://localhost:3000/'],
                  responseType: 'code' // or 'token', note that REFRESH token will only be generated when the responseType is code
                }
              }
              */
            }
          }
        });
        setCognitoConfigured(true);
      }
    }, [config]);

  // Check if a user is already signed in
  useEffect(() => {
    if (cognitoConfigured) {
      const checkUser = async () => {
        try {
          const { username } = await getCurrentUser();
          console.log("User already present: ", username)
          // Here we capture the username but setUser when login doesn't see the TODO
          setUser(username);
        } catch (error) {
          console.error("Could not find existing user:", error);
          setUser(null); // No user is signed in
        }
      };
      checkUser();
    }
  }, [cognitoConfigured]);

  useEffect(() => {
    const loadQuestions = async () => {
      if (!config) return;
      const fetchedQuestions = await fetchQuestions(config.apiUrl);
      setQuestions(fetchedQuestions);
      setIsFetchingQuestions(false);
    };

    loadQuestions();
  }, [config]);

  // Handle sign in
  const handleLogin = async (username, password) => {
    try {
      const user = await signIn({ username, password });
      // TODO: Make user object actually hold user data like username
      // Currently it stores next steps.
      setUser(user); 
      console.log("Logged in as:", user);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const handleSignUp = async (username, password, email) => {
    try {
      // Use the updated structure with an options object
      const { user } = await signUp({
        username,
        password,
        options: {
          userAttributes: {
            email,
          },
          autoSignIn: true
        }
      });
      
      console.log("Sign-up successful:", user);
    } catch (error) {
      console.error("Sign-up failed:", error);
    }
  };

  const handleResendCode = async (username) => {
    try {
      await resendSignUpCode({ username });
      console.log("Verification code resent");
    } catch (error) {
      console.error("Resend code failed:", error);
    }
  };

  const handleVerify = async (username, confirmationCode) => {
    try {
      await confirmSignUp({ username, confirmationCode });
      console.log("Verification successful");
      // Optionally auto-login or redirect after verification
    } catch (error) {
      console.error("Verification failed:", error);
    }
  };

  const handleLogout = async () => {
    try {
      await signOut();
      setUser(null);
      console.log("Logged out");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  const handleSelectedAnswer = (event) => {
    setSelectedAnswer(Number(event.target.value));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const currentQuestion = questions[currentQuestionIndex];
    if (selectedAnswer === currentQuestion?.correctAnswer) {
      setScore((prevScore) => prevScore + 1);
    }
    setIsSubmitted(true)
  };

  const handleNextQuestion = (event) => {
    event.preventDefault();

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
      setSelectedAnswer(null);
    } else {
      setIsQuizCompleted(true);
    }
    setIsSubmitted(false)
  };

  const handlePlayAgain = () => {
    setIsQuizCompleted(false);
    setCurrentQuestionIndex(0);
    setScore(0);
    setSelectedAnswer(null);
  };

  if (isFetchingQuestions) {
    return <div>Loading quiz...</div>;
  }

  const currentQuestion = questions[currentQuestionIndex];
  const boardHeaderText = `${currentQuestionIndex + 1} / ${questions.length}`;

  // Render loading screen while configuration is not yet loaded
  if (!config) return <div>Loading configuration...</div>;

  // Render login screen if user is not logged in
  if (!user) {
    return (
      <Login
        onLogin={handleLogin}
        onSignUp={handleSignUp}
        onVerify={handleVerify}
        onResend={handleResendCode}
      />
    );
  }
  
  return isQuizCompleted ? (
    <ResultBoard
      score={score}
      totalQuestions={questions.length}
      onPlayAgain={handlePlayAgain}
    />
  ) : (
    <QuestionBoard
      onSubmit={handleSubmit}
      onNextQuestion={handleNextQuestion}
      isSubmitted={isSubmitted}
      question={currentQuestion}
      headerText={boardHeaderText}
      onSelectedAnswer={handleSelectedAnswer}
      selectedAnswer={selectedAnswer}
    />
  );
}

export default App;
