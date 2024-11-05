import React from 'react';

function QuestionBoard({ onSubmit, question, headerText, onSelectedAnswer, selectedAnswer }) {
  return (
    <div id="questionApp">
      <div id="questionHeader">
        <h1>Quiz</h1>
      </div>
      <form onSubmit={onSubmit} id="questionForm">
        <h1>{headerText}</h1>
        <p>{question.text}</p>
        {question.answers.map((answer, index) => (
          <React.Fragment key={index}>
            <input
              type="radio"
              value={index}
              onChange={onSelectedAnswer}
              name="radioAnswer"
              id={`q${index}`}
              checked={selectedAnswer === index}
            />
            <label htmlFor={`q${index}`}> {answer}</label>
            <br />
          </React.Fragment>
        ))}
        <button type="submit" disabled={selectedAnswer === null}>Submit</button>
      </form>
    </div>
  );
}

export default QuestionBoard;
