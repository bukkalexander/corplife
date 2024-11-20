import React from 'react';

function UserBanner({ username, userXp, onLogout }) {
  return (
    <div id="userBanner">
      <span>Welcome, {username}!</span>
      {userXp !== null && (
        <span className="user-xp">| XP : {userXp}</span>
      )}
      <button onClick={onLogout} className="secondary-button">
        Logout
      </button>
    </div>
  );
}

export default UserBanner;
