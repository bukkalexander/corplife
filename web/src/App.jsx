import React, { useState, useEffect } from 'react';
import QuestionBoard from './QuestionBoard.jsx';
import ResultBoard from './ResultBoard.jsx';
// import config from './Config.js';

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
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
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
      const fetchedQuestions = await fetchQuestions(config.api_url);
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

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
      setSelectedAnswer(null);
    } else {
      setIsQuizCompleted(true);
    }
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

  return isQuizCompleted ? (
    <ResultBoard
      score={score}
      totalQuestions={questions.length}
      onPlayAgain={handlePlayAgain}
    />
  ) : (
    <QuestionBoard
      onSubmit={handleSubmit}
      question={currentQuestion}
      headerText={boardHeaderText}
      onSelectedAnswer={handleSelectedAnswer}
      selectedAnswer={selectedAnswer}
    />
  );
}

export default App;
