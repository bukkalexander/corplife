import React from 'react';

function QuestionBoard({ onSubmit, onNextQuestion, isSubmitted, question, headerText, onSelectedAnswer, selectedAnswer }) {
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
              disabled={isSubmitted}
            />
            <label 
              htmlFor={`q${index}`}
              style={{
                color: isSubmitted && index === question.correctAnswer ? 'green' : 
                      isSubmitted && index === selectedAnswer && index !== question.correctAnswer ? 'red' : 'black'
              }}
            >
              {answer}
            </label>
            <br />
          </React.Fragment>
        ))}
        {
          isSubmitted ?
          <button type="button" onClick={onNextQuestion} className="primary-button">Next</button>
          :
          <button type="submit" disabled={selectedAnswer === null} className="primary-button">Submit</button>
        }
      </form>
    </div>
  );
}

export default QuestionBoard;
