import React, { useState } from 'react';
import QuestionBoard from './QuestionBoard.jsx';
import ResultBoard from './ResultBoard.jsx';

const questionList = [
  {
    text: 'What kind of storage is AWS S3',
    answers: ['Object storage', 'SQL database', 'Block storage', 'Document database'],
    correctAnswer: 0,
  },
  {
    text: 'What does EC2 mean',
    answers: ['Elastic Container Creater', 'Elastic Compute Cloud', 'Ephemeral Code Catalog', 'Error Cloud 2'],
    correctAnswer: 1,
  },
];

function App() {
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);

  const handleSelectedAnswer = (event) => {
    setSelectedAnswer(Number(event.target.value));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(selectedAnswer);

    if (selectedAnswer == questionList[currentQuestionIndex].correctAnswer) {
      setScore(score + 1);
    }

    if (currentQuestionIndex < questionList.length - 1) {
      if (selectedAnswer == questionList[currentQuestionIndex].correctAnswer) {
        setScore(score + 1);
      }
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setIsQuizCompleted(true)
    }
  };

  const question = questionList[currentQuestionIndex];
  const boardHeaderText = `${currentQuestionIndex + 1} / ${questionList.length}`;
  return isQuizCompleted ? (
    <ResultBoard score={score} totalQuestions={questionList.length} />
  ) : (
    <QuestionBoard
      onSubmit={handleSubmit}
      question={question}
      headerText={boardHeaderText}
      onSelectedAnswer={handleSelectedAnswer}
    />
  );
}

export default App;
