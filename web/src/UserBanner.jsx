import React from 'react';

function UserBanner({ username, userScore, onLogout }) {
  return (
    <div id="userBanner">
      <span>Welcome, {username}!</span>
      {userScore !== null && (
        <span className="user-score">| Cumulative Score: {userScore}</span>
      )}
      <button onClick={onLogout} className="secondary-button">
        Logout
      </button>
    </div>
  );
}

export default UserBanner;
