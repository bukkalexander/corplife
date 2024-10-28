import React from 'react';

function ResultBoard({ score, totalQuestions, onPlayAgain }) {
  const scoreSummary = `${score} / ${totalQuestions}`;
  const message =
    score === totalQuestions
      ? 'Congratulations, you got a perfect score!'
      : 'Great job, keep practicing!';
  return (
    <div id="resultBoard">
      <h1>Quiz Completed!</h1>
      <p>Your Score: {scoreSummary}</p>
      <p>{message}</p>
      <button onClick={onPlayAgain}>Play Again</button>
    </div>
  );
}

export default ResultBoard;
