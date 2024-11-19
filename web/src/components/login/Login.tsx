import React, { useEffect, useState } from 'react';
import { Amplify } from 'aws-amplify';
import { signIn, signUp, resendSignUpCode, confirmSignUp, getCurrentUser } from '@aws-amplify/auth';
import { fetchConfig } from '@features/config';
import Form from '@components/common/Form';
import { H1, P } from '@components/common/Typography';
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
  const { user, dispatch: dispatchUser } = useUserContext();
  const [loginState, setLoginState] = useState<LoginState>(LoginState.SIGNIN);
  const [isCognitoConfigured, setIsCognitoConfigured] = useState<boolean>(false);
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [verificationCode, setVerificationCode] = useState('');

  useEffect(() => {
    const configureCognito = async () => {
      const config = await fetchConfig();
      if (!config) return;
      /* eslint-disable @typescript-eslint/no-explicit-any */
      Amplify.configure({
        Auth: {
          Cognito: {
            userPoolId: config.userPoolId,
            userPoolClientId: config.userPoolWebClientId,
            allowGuestAccess: true,
            //OPTIONAL - This is used when autoSignIn is enabled for Auth.signUp
            // 'code' is used for Auth.confirmSignUp, 'link' is used for email link verification
            //signUpVerificationMethod: 'code', // 'code' | 'link'
            /*
              loginWith: {
                // OPTIONAL - Hosted UI configuration
                oauth: {
                  domain: 'your_cognito_domain',
                  scopes: [
                    'phone',
                    'email',
                    'profile',
                    'openid',
                    'aws.cognito.signin.user.admin'
                  ],
                  redirectSignIn: ['http://localhost:3000/'],
                  redirectSignOut: ['http://localhost:3000/'],
                  responseType: 'code' // or 'token', note that REFRESH token will only be generated when the responseType is code
                }
              }
              */
          },
        },
      } as any); // TODO: can't get types to work here
      /* eslint-enable @typescript-eslint/no-explicit-any */

      setIsCognitoConfigured(true);
    };
    configureCognito();
  }, []);

  // Check if a user is already signed in
  useEffect(() => {
    if (isCognitoConfigured) {
      const loadCurrentUser = async () => {
        try {
          const { username: amplify_username } = await getCurrentUser();
          console.log('User already present: ', amplify_username);
          dispatchUser({
            type: UserActionType.SET_USER,
            payload: {
              id: '0', // TODO: get user id
              username: amplify_username,
            },
          });
        } catch (error) {
          console.error('Could not find existing user:', error);
        }
      };
      loadCurrentUser();
    }
  }, [isCognitoConfigured, dispatchUser]);

  const handleSignin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await signIn({ username, password });
      const { username: amplify_username } = await getCurrentUser();
      const id = '0'; // TODO: get user id
      dispatchUser({
        type: UserActionType.SET_USER,
        payload: {
          id,
          username: amplify_username,
        },
      });
      console.log('Logged in as:', username);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const handleSignUp = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const signUpOutput = await signUp({
        username,
        password,
        options: {
          userAttributes: {
            email,
          },
          autoSignIn: true,
        },
      });
      console.log('Sign-up successful:', signUpOutput);
      setLoginState(LoginState.VERIFY);
    } catch (error) {
      console.error('Sign-up failed:', error);
    }
  };

  const handleSubmitVerificationCode = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await confirmSignUp({ username, confirmationCode: verificationCode });
      console.log('Verification successful');
      console.log('Attempting to log in...');
      handleSignin(e);
    } catch (error) {
      console.error('Verification failed:', error);
    }
  };

  const handleResendVerificationCode = async () => {
    try {
      await resendSignUpCode({ username });
      console.log('Verification code resent');
    } catch (error) {
      console.error('Resend code failed:', error);
    }
  };

  const handleGuestLogin = () => {
    dispatchUser({
      type: UserActionType.SET_USER,
      payload: {
        id: 'guest',
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

  if (user) return null;

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
            <P>Not ready to submit code?</P>
            <div className="flex flex-row w-full justify-center gap-4">
              <Button
                variant="secondary"
                onClick={() => confirmSignUp({ username, confirmationCode: verificationCode })}
              >
                Verify Code
              </Button>
              <Button variant="secondary" onClick={handleResendVerificationCode}>
                Resend Code
              </Button>
            </div>
            <GuestLink onClick={handleGuestLogin} />
          </div>
        </Content>
      );

    default:
      return null;
  }
};

export default Login;
