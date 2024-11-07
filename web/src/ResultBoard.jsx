import React from 'react';

function ResultBoard({ score, totalQuestions, onPlayAgain }) {
  const scoreSummary = `${score} / ${totalQuestions}`;
  const message =
    score === totalQuestions
      ? 'Congratulations, you got a perfect score!'
      : 'Great job, keep practicing!';

  return (
    <div id="questionApp"> {/* Reuse #questionApp styles for consistency */}
      <div id="resultBoardHeader">
        <h1>Quiz Completed!</h1>
      </div>
      <p>Your Score: {scoreSummary}</p>
      <p>{message}</p>
      <button onClick={onPlayAgain} className="primary-button">
        Play Again
      </button>
    </div>
  );
}

export default ResultBoard;
