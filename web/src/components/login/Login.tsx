import React, { useState } from 'react';
import Form from '@components/common/Form';
import { P } from '@components/common/Typography';
import Button from '@components/common/Button';
import UsernameInput from '@components/login/UsernameInput';
import PasswordInput from '@components/login/Password';
import GuestLink from '@components/login/GuestLink';
import EmailInput from '@components/login/EmailInput';
import VerificationCodeInput from '@components/login/VerificationInput';
import { UserActionType, useUserContext } from '@features/user';
import { Content } from '@components/common/Layout';

enum LoginState {
  SIGNIN,
  SIGNUP,
  VERIFY,
}

const Login: React.FC = () => {
  const User = useUserContext();
  const [loginState, setLoginState] = useState<LoginState>(LoginState.SIGNIN);
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [verificationCode, setVerificationCode] = useState('');

  const handleSignin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await User.signIn(username, password);
      console.log('Logged in as:', username);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const handleSignUp = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await User.signUp(username, password, email);
      console.log('Sign-up successful for: ', username);
      setLoginState(LoginState.VERIFY);
    } catch (error) {
      console.error('Sign-up failed:', error);
    }
  };

  const handleSubmitVerificationCode = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await User.confirmSignUp(username, verificationCode);
      console.log('Verification successful');
      console.log('Attempting to log in...');
      handleSignin(e);
    } catch (error) {
      console.error('Verification failed:', error);
    }
  };

  const handleResendVerificationCode = async () => {
    try {
      await User.resendSignUpCode(username);
      console.log('Verification code resent');
    } catch (error) {
      console.error('Resend code failed:', error);
    }
  };

  const handleGuestLogin = () => {
    User.dispatch({
      type: UserActionType.SET_USER,
      payload: {
        id: 'Guest',
        username: 'Guest',
      },
    });
  };

  const handleUsernameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };
  const handleVerificationCodeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setVerificationCode(e.target.value);
  };

  switch (loginState) {
    case LoginState.SIGNIN:
      return (
        <Content>
          <Form onSubmit={handleSignin}>
            <UsernameInput value={username} onChange={handleUsernameChange} />
            <PasswordInput value={password} onChange={handlePasswordChange} />
            <Button variant="primary" type="submit">
              Login
            </Button>
          </Form>
          <hr className="w-full mt-2" />
          <div className="flex flex-col items-center w-full gap-2">
            <P>New user?</P>
            <div className="flex flex-col w-1/2">
              <Button
                variant="secondary"
                onClick={() => {
                  setLoginState(LoginState.SIGNUP);
                }}
              >
                Sign Up
              </Button>
            </div>

            <GuestLink onClick={handleGuestLogin} />
          </div>
        </Content>
      );

    case LoginState.SIGNUP:
      return (
        <Content>
          <Form onSubmit={handleSignUp}>
            <UsernameInput value={username} onChange={handleUsernameChange} />
            <EmailInput value={email} onChange={handleEmailChange} />
            <PasswordInput value={password} onChange={handlePasswordChange} />
            <Button type="submit">Sign Up</Button>
            <hr className="w-full mt-2" />
            <div className="flex flex-col items-center w-full gap-2">
              <P>Already have an account?</P>
              <div className="flex flex-col w-1/2">
                <Button
                  variant="secondary"
                  onClick={() => {
                    setLoginState(LoginState.SIGNIN);
                  }}
                >
                  Login
                </Button>
              </div>
              <GuestLink onClick={handleGuestLogin} />
            </div>
          </Form>
        </Content>
      );

    case LoginState.VERIFY:
      return (
        <Content>
          <Form onSubmit={handleSubmitVerificationCode}>
            <UsernameInput value={username} onChange={handleUsernameChange} />
            <VerificationCodeInput
              value={verificationCode}
              onChange={handleVerificationCodeChange}
            />
            <Button type="submit">Submit Code</Button>
          </Form>
          <hr className="w-full mt-2" />
          <div className="flex flex-col items-center w-full gap-2">
            <P>Code not working?</P>
            <Button variant="secondary" onClick={handleResendVerificationCode}>
              Resend Code
            </Button>
            <GuestLink onClick={handleGuestLogin} />
          </div>
        </Content>
      );

    default:
      return null;
  }
};

export default Login;
