import React, { useState, useEffect } from 'react';
import { Amplify } from 'aws-amplify';
import {
  signIn,
  signUp,
  signOut,
  resendSignUpCode,
  confirmSignUp,
  getCurrentUser,
  fetchAuthSession,
} from '@aws-amplify/auth';

import Login from './Login.jsx';
import UserBanner from './UserBanner.jsx';
import QuestionBoard from './QuestionBoard.jsx';
import LeaderBoard from './LeaderBoard.jsx';

const CONFIG_URL = './config.json';

const fetchConfig = async (configUrl) => {
  try {
    console.log('Fetching config...');
    const response = await fetch(configUrl);
    console.log('Fetching config DONE');
    if (!response.ok) {
      throw new Error(`Failed to fetch config: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching config:', error);
    return null;
  }
};

const fetchQuestions = async (apiUrl) => {
  const fetchQuestionsUrl = `${apiUrl}/questions`;
  console.log(fetchQuestionsUrl);
  try {
    console.log('Fetching questions...');
    const response = await fetch(fetchQuestionsUrl);

    console.log('Fetching questions DONE');
    if (!response.ok) {
      throw new Error(`Failed to fetch: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching questions:', error);
    return [];
  }
};

const postScore = async (apiUrl, scoreData) => {
  const postScoreUrl = `${apiUrl}/score`;
  try {
    console.log('Posting score...');
    const response = await fetch(postScoreUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(scoreData),
    });
    console.log('Posting score DONE');
    if (!response.ok) {
      throw new Error(`Failed to post score: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error posting score:', error);
    return null;
  }
};

const fetchScores = async (apiUrl) => {
  const fetchScoresUrl = `${apiUrl}/scores`;
  try {
    console.log('Fetching all scores...');
    const response = await fetch(fetchScoresUrl);
    console.log('Fetching all scores DONE');
    if (!response.ok) {
      throw new Error(`Failed to fetch scores: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching scores:', error);
    return [];
  }
};

const fetchUserScore = async (api_url, user) => {
  if (!user || user === "Guest") {
    console.log("Skipping score fetch for Guest or no user");
    return null;
  }

  const fetchScoreUrl = `${api_url}/user/score`;
  try {
    console.log("Fetching user score...");

    const session = await fetchAuthSession();
    const idToken = session.tokens.idToken;

    const response = await fetch(fetchScoreUrl, {
      headers: {
        Authorization: `${idToken}`,
      },
    });

    if (!response.ok) {
      // Log error details from the response
      const errorData = await response.json();
      console.error("Error fetching user score:", errorData.detail);
      return null;
    }

    const data = await response.json();
    return { username: data.username, score: data.score };
  } catch (error) {
    console.error("Error fetching user score:", error.message);
    return null;
  }
};

function App() {
  const [config, setConfig] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [scoreData, setScoreData] = useState(null);
  const [scoreDataList, setScoreDataList] = useState([]);
  const [isFetchingQuestions, setIsFetchingQuestions] = useState(true);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [user, setUser] = useState(null);
  const [userScore, setUserScore] = useState(null); // Cumulative score from backend
  const [cognitoConfigured, setCognitoConfigured] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const loadConfig = async () => {
      const fetchedConfig = await fetchConfig(CONFIG_URL);
      console.log(fetchedConfig);
      setConfig(fetchedConfig);
    };
    console.log('Loading config...');
    loadConfig();
    console.log('Loading config DONE');
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
          },
        },
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
          console.log('User already present: ', username);
          setUser(username);
        } catch (error) {
          console.error('Could not find existing user:', error);
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

  useEffect(() => {
    const loadUserScore = async () => {
      if (!config || !user || user === "Guest") {
        setUserScore(null); // Default userScore for Guest or no user
        return;
      }
  
      const fetchedUserScore = await fetchUserScore(config.apiUrl, user);
      if (fetchedUserScore) {
        setUserScore(fetchedUserScore.score); // Set the cumulative score
      }
    };
  
    loadUserScore();
  }, [config, user]);
  

  const handleLogin = async (username, password) => {
    try {
      const user = await signIn({ username, password });
      setUser(username);
      setErrorMessage('');
      console.log('Logged in as:', username);
    } catch (error) {
      console.error('Login failed:', error);
      setErrorMessage('Incorrect username or password.');
    }
  };

  const handleSignUp = async (username, password, email) => {
    try {
      const { user } = await signUp({
        username,
        password,
        options: {
          userAttributes: {
            email,
          },
          autoSignIn: true,
        },
      });
setErrorMessage('');
      console.log('Sign-up successful:', user);
      return true;
    } catch (error) {
      console.error('Sign-up failed:', error);
      setErrorMessage('Sign-up failed. Please check your details and try again.');
      return false;
    }
  };

  const handleResendCode = async (username) => {
    try {
      await resendSignUpCode({ username });
      setErrorMessage('');
      console.log('Verification code resent');
    } catch (error) {
      console.error('Resend code failed:', error);
      setErrorMessage('Failed to resend verification code. Please try again.');
    }
  };

  const handleVerify = async (username, confirmationCode) => {
    try {
      await confirmSignUp({ username, confirmationCode });
      setErrorMessage(''); // Clear any error messages
      console.log('Verification successful');
      return true; // Indicate that verification was successful
    } catch (error) {
      console.error('Verification failed:', error);
      setErrorMessage('Verification failed. Please check your code and try again.');
      return false; // Indicate verification failed
    }
  };

  const handleLogout = async () => {
    try {
      await signOut();
      setUser(null);
      console.log('Logged out');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  const handleGuestLogin = () => {
    setUser('Guest'); // Set an arbitrary guest username
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
    setIsSubmitted(true);
  };

  const handleNextQuestion = (event) => {
    event.preventDefault();

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
      setSelectedAnswer(null);
    } else {
      setIsQuizCompleted(true);
      const scoreData = {
        id: null,
        score: score,
        nbrOfQuestions: questions.length,
        timestamp: null,
      };
      postScore(config.apiUrl, scoreData).then((scoreDataResponse) => {
        setScoreData(scoreDataResponse);
      });
    }
    setIsSubmitted(false);
  };

  useEffect(() => {
    if (isQuizCompleted && scoreData && config) {
      fetchScores(config.apiUrl).then((data) => {
        setScoreDataList(data);
      });
    }
  }, [isQuizCompleted, scoreData, config]);

  const handlePlayAgain = () => {
    setIsQuizCompleted(false);
    setCurrentQuestionIndex(0);
    setScore(0);
    setSelectedAnswer(null);
  };

  const currentQuestion = questions[currentQuestionIndex];
  const boardHeaderText = `${currentQuestionIndex + 1} / ${questions.length}`;

  // Render loading screen while configuration is not yet loaded
  if (!config) return <div>Loading configuration...</div>;
  if (isFetchingQuestions) return <div>Loading quiz...</div>;

  // Render login screen if user is not logged in
  if (!user) {
    return (
      <Login
        onLogin={handleLogin}
        onSignUp={handleSignUp}
        onVerify={handleVerify}
        onResend={handleResendCode}
        onGuestLogin={handleGuestLogin}
        errorMessage={errorMessage}
      />
    );
  }

  return (
    <>
      {/* Display UserBanner if the user is logged in */}
      {user && (
        <UserBanner
          username={user}
          userScore={userScore}
          onLogout={handleLogout}
        />
      )}

      {isQuizCompleted ? (
        <LeaderBoard
          scoreData={scoreData}
          scoreDataList={scoreDataList}
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
      )}
    </>
  );
}

export default App;
