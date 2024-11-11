import React from 'react';

function UserBanner({ username, onLogout }) {
  return (
    <div id="userBanner">
      <span>Welcome, {username}!</span>
      <button onClick={onLogout} className="secondary-button">
        Logout
      </button>
    </div>
  );
}

export default UserBanner;
