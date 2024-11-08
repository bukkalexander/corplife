import React, { useState, useEffect } from 'react';
import QuestionBoard from './QuestionBoard.jsx';
import LeaderBoard from './LeaderBoard.jsx';

const CONFIG_URL = "./config.json";

const fetchConfig = async (configUrl) => {
  try {
    console.log("Fetching config...")
    const response = await fetch(configUrl);
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

const fetchQuestions = async (apiUrl) => {

  const fetchQuestionsUrl = `${apiUrl}/questions` ;
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

const postScore = async (apiUrl, scoreData) => {
  const postScoreUrl = `${apiUrl}/score`;
  try {
    console.log("Posting score...");
    const response = await fetch(postScoreUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(scoreData)
    });
    console.log("Posting score DONE");
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
    console.log("Fetching all scores...");
    const response = await fetch(fetchScoresUrl);
    console.log("Fetching all scores DONE");
    if (!response.ok) {
      throw new Error(`Failed to fetch scores: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching scores:', error);
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
  const [scoreData, setScoreData] = useState(null);
  const [scoreDataList, setScoreDataList] = useState([]);
  
  const [isFetchingQuestions, setIsFetchingQuestions] = useState(true);

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


  useEffect(() => {
    const loadQuestions = async () => {
      if (!config) return;
      const fetchedQuestions = await fetchQuestions(config.apiUrl);
      setQuestions(fetchedQuestions);
      setIsFetchingQuestions(false);
    };

    loadQuestions();
  }, [config]);

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
      const scoreData = {
        id: null,
        score: score,
        nbrOfQuestions: questions.length,
        timestamp: null
      }
      postScore(config.apiUrl, scoreData).then(
        (scoreDataResponse) => {
          setScoreData(scoreDataResponse);
        }
      );
    }
    setIsSubmitted(false)
  };

  useEffect(() => {
    if (isQuizCompleted && scoreData && config) {
      fetchScores(config.apiUrl).then(
        (data) => {
          setScoreDataList(data);
        }
      );
    }
  }, [isQuizCompleted, scoreData, config]);

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

  return isQuizCompleted ? (
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
  );
}

export default App;
