import React from 'react'

function App() {
  const question = {text:"What does AWS S3 do",answers:["S3 bla 1","S3 bla 2","S3 bla 3","S3 bla 4"]};
  return (
      <div id="questionApp">
        <div id="questionHeader">
          <h1>"Quiz"</h1>
        </div>
        <form id="questionForm">
          <h1>1/20</h1>
          <p>{question.text}</p>
          {question.answers.map((answer, index) => (
            <>
              <input type="radio" name={`q${index}`} />
              <label htmlFor={`q${index}`}> {answer}</label><br />
            </>
          ))}
          <button type="submit">Submit</button>
        </form>
      </div>
  )
}

export default App;
