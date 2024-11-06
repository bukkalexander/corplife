import React, { useState } from 'react';

function Login({ onLogin, onSignUp, onVerify, onResend }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [isSignUp, setIsSignUp] = useState(false);
  const [isVerifying, setIsVerifying] = useState(false);
  const [verificationCode, setVerificationCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isVerifying) {
      onVerify(username, verificationCode); // Verify the code
    } else if (isSignUp) {
      onSignUp(username, password, email).then(() => setIsVerifying(true)); // Initiate sign-up and switch to verification
    } else {
      onLogin(username, password);
    }
  };

  return (
    <div id="loginApp">
      <div id="loginHeader">
        <h1>{isVerifying ? "Verify Account" : isSignUp ? "Sign Up" : "Login"}</h1>
      </div>
      <form onSubmit={handleSubmit} id="loginForm">
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <br />

        {isSignUp && !isVerifying && (
          <>
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <br />
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
            />
            <br />
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
            />
            <button type="button" onClick={() => onVerify(username, verificationCode)}>
              Verify
            </button>
            <button type="button" onClick={() => onResend(username)}>
              Resend Code
            </button>
            <br />
          </>
        )}

        <button type="submit">
          {isVerifying ? "Submit Code" : isSignUp ? "Sign Up" : "Login"}
        </button>

        {!isVerifying && (
          <button type="button" onClick={() => setIsSignUp(!isSignUp)}>
            {isSignUp ? "Already have an account? Login" : "New user? Sign Up"}
          </button>
        )}
      </form>
    </div>
  );
}

export default Login;
