import React, { useState, useEffect } from 'react';
import QuestionBoard from './QuestionBoard.jsx';
import ResultBoard from './ResultBoard.jsx';
import config from './Config.js';

const fetchQuestions = async () => {
  const fetchQuestionsUrl = `${config.API_URL}/questions` ;
  try {
    const response = await fetch(fetchQuestionsUrl);
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
  const [questions, setQuestions] = useState([]);
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [isFetchingQuestions, setIsFetchingQuestions] = useState(true);

  useEffect(() => {
    const loadQuestions = async () => {
      const fetchedQuestions = await fetchQuestions();
      setQuestions(fetchedQuestions);
      setIsFetchingQuestions(false);
    };

    loadQuestions();
  }, []);

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
