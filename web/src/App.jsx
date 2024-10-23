import React , { useState, useEffect } from 'react';

const questionList = [
  {text:"Q1 What does AWS S3 do",answers:["S3 bla 1","S3 bla 2","S3 bla 3","S3 bla 4"]}, 
  {text:"Q2 What does EC2 mean",answers:["S3 bla 1","S3 bla 2","S3 bla 3","S3 bla 4"]}
];

function App() {
  const [selectedOption, setSelectedOption] = useState(null);

  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

  // Get the current question from questionList
  const question = questionList[currentQuestionIndex];

  // Handle change when radio button is selected
  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  // Handle form submit
  const handleSubmit = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    console.log(selectedOption);

    // Move to the next question if available
    if (currentQuestionIndex < questionList.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      console.log("End of questions");
    }
  };

  return (
      <div id="questionApp">
        <div id="questionHeader">
          <h1>Quiz</h1>
        </div>
        <form onSubmit={handleSubmit} id="questionForm">
          <h1>{currentQuestionIndex+1}/{questionList.length}</h1>
          <p>{question.text}</p>
          {question.answers.map((answer, index) => (
            <>
              <input type="radio" value={index} onChange={handleOptionChange} name="radioAnswer" id={`q${index}`} />
              <label htmlFor={`q${index}`}> {answer}</label><br />
            </>
          ))}
          <button type="submit">Submit</button>
        </form>
      </div>
  )
}

export default App;
