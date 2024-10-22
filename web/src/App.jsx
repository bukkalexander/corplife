import React from 'react'

function App() {

  return (
      <div id="questionApp">
        <div id="questionHeader">
          <h1>Question Text</h1>
        </div>
        <form id="questionForm">
          <h1>1/20</h1>
          <p>What does AWS S3 do</p>
          <input type="radio" name="q1" />
          <label htmlFor="q1"> S3 bla 1</label><br />
          <input type="radio" name="q2" />
          <label htmlFor="q2"> S3 bla 2</label><br />
          <input type="radio" name="q3" />
          <label htmlFor="q3"> S3 bla 3</label><br />
          <input type="radio" name="q4" />
          <label htmlFor="q4"> S3 bla 4</label><br />
          <button type="submit">Submit</button>
        </form>
      </div>
  )
}

export default App;
