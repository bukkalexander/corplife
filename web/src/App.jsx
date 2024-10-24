import React, { useState } from 'react';
import QuestionBoard from './QuestionBoard.jsx'
import ResultBoard from './ResultBoard.jsx'

const questionList = [
  {text:"Q1 What does AWS S3 do",answers:["S3 bla 1","S3 bla 2","S3 bla 3","S3 bla 4"], correctAnswer: 0 }, 
  {text:"Q2 What does EC2 mean",answers:["S3 bla 1","S3 bla 2","S3 bla 3","S3 bla 4"], correctAnswer: 1 }
];

function App() {

  const [isQuizCompleted, setIsQuizCompleted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  
  const handleSelectedAnswer = (event) => {
    setSelectedAnswer(event.target.value);
  };

  const handleIsQuizCompleted = () => {
    setIsQuizCompleted(true);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(selectedAnswer);

    if (currentQuestionIndex < questionList.length - 1) {
      if (selectedAnswer == questionList[currentQuestionIndex].correctAnswer) {
        setScore(score + 1);
      }
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      handleIsQuizCompleted();
    }
  };

  const question = questionList[currentQuestionIndex];
  const boardHeaderText = `${currentQuestionIndex + 1} / ${questionList.length}`;
  return (
    <>{ isQuizCompleted ? <ResultBoard score={score} totalQuestions={questionList.length} /> : <QuestionBoard onSubmit={handleSubmit} question={question} headerText={boardHeaderText} onSelectedAnswer={handleSelectedAnswer}/> }</>
  )
}

export default App;
