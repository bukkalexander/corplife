import React from 'react';
import { format } from 'date-fns';
import './LeaderBoard.css';

function LeaderBoard({ scoreData, scoreDataList, onPlayAgain }) {
  return (
    <div className="quizBoard">
      <h1>LeaderBoard</h1>
      <table className="leaderboard-table">
        <thead>
          <tr>
            <th>Score</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {scoreDataList.map((data) => (
            <tr
              key={data.id}
              className={data.id === scoreData.id ? 'highlight' : ''}
            >
              <td>{data.score} / {data.nbrOfQuestions}</td>
              <td>{format(new Date(data.timestamp), 'yyyy-MM-dd HH:mm')}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={onPlayAgain}>Play Again</button>
    </div>
  );
}

export default LeaderBoard;
