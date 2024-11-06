import React from 'react';
import './LeaderBoard.css';

function LeaderBoard({ scoreData, scoreDataList, onPlayAgain }) {
  return (
    <div className="leaderboard-container">
      <h1>LeaderBoard</h1>
      <table className="leaderboard-table">
        <thead>
          <tr>
            <th>Score</th>
            <th>Number of Questions</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {scoreDataList.map((data) => (
            <tr
              key={data.id}
              className={data.id === scoreData.id ? 'highlight' : ''}
            >
              <td>{data.score}</td>
              <td>{data.nbrOfQuestions}</td>
              <td>{data.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="play-again-button" onClick={onPlayAgain}>Play Again</button>
    </div>
  );
}

export default LeaderBoard;
