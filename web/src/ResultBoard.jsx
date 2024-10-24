import React from 'react';

function ResultBoard({score, totalQuestions}) {

  return (
    <div id="resultBoard">
      <h1>Quiz Completed!</h1>
      <p>Your Score: {score} / {totalQuestions}</p>
      <p>{score === totalQuestions ? 'Congratulations, you got a perfect score!' : 'Great job, keep practicing!'}</p>
    </div>
  )
}

export default ResultBoard;
