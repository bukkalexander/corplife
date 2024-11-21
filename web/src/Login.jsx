import React, { useState } from 'react';

function Login({ onLogin, onSignUp, onVerify, onResend, onGuestLogin, errorMessage }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [isSignUp, setIsSignUp] = useState(false);
  const [isVerifying, setIsVerifying] = useState(false);
  const [verificationCode, setVerificationCode] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isVerifying) {
      const verificationSuccessful = await onVerify(username, verificationCode);
      if (verificationSuccessful) {
        setIsVerifying(false); // Reset to login view after verification
        setIsSignUp(false);     // Ensure it's back to login mode
      }
    } else if (isSignUp) {
      const signUpSuccessful = await onSignUp(username, password, email);
      if (signUpSuccessful) {
        setIsVerifying(true); // Only proceed to verification if sign-up is successful
      }
    } else {
      onLogin(username, password);
    }
  };

  return (
    <div className="container-card">
      <h1 className="header-text">
        {isVerifying ? 'Verify Account' : isSignUp ? 'Sign Up' : 'Login'}
      </h1>
      <form onSubmit={handleSubmit} id="loginForm">
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          className="form-input"
        />

        {isSignUp && !isVerifying && (
          <>
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="form-input"
            />
          </>
        )}

        {!isVerifying && (
          <>
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="form-input"
            />
          </>
        )}

        {isVerifying && (
          <>
            <label htmlFor="verificationCode">Verification Code:</label>
            <input
              type="text"
              id="verificationCode"
              value={verificationCode}
              onChange={(e) => setVerificationCode(e.target.value)}
              required
              className="form-input"
            />
            <div className="verification-buttons">
              <button
                type="button"
                onClick={() => onVerify(username, verificationCode)}
              >
                Verify
              </button>
              <button type="button" onClick={() => onResend(username)}>
                Resend Code
              </button>
            </div>
          </>
        )}

        {errorMessage && <p className="error-message">{errorMessage}</p>}

        <button type="submit" className="primary-button">
          {isVerifying ? 'Submit Code' : isSignUp ? 'Sign Up' : 'Login'}
        </button>

        {!isVerifying && (
          <button
            type="button"
            onClick={() => setIsSignUp(!isSignUp)}
            className="secondary-button"
          >
            {isSignUp ? 'Already have an account? Login' : 'New user? Sign Up'}
          </button>
        )}

        <div className="guest-access">
          <a
            href="#continue-as-guest"
            onClick={(e) => {
              e.preventDefault();
              onGuestLogin();
            }}
            className="guest-link"
          >
            Continue as Guest
          </a>
        </div>
      </form>
    </div>
  );
}

export default Login;
