import React, { useEffect, useState } from 'react';
import { UserActionType, UserProviderProps } from '@features/user/types';
import { useUserReducer } from '@features/user/hooks';
import { UserContext } from '@features/user/Context';
import { fetchConfig } from '@features/config';
import { Amplify } from 'aws-amplify';
import * as Auth from 'aws-amplify/auth';

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
  const { user, dispatch } = useUserReducer();
  const [isLoading, setIsLoading] = useState(true);
  const [isAmplifyConfigured, setIsAmplifyConfigured] = useState(false);

  useEffect(() => {
    const configureAmplify = async () => {
      if (isAmplifyConfigured) return;

      const config = await fetchConfig();
      if (!config) return;

      /* eslint-disable @typescript-eslint/no-explicit-any */
      // NOTE: Amplify auth docs: https://docs.amplify.aws/react/build-a-backend/auth/connect-your-frontend/
      Amplify.configure({
        Auth: {
          Cognito: {
            userPoolId: config.userPoolId,
            userPoolClientId: config.userPoolWebClientId,
            allowGuestAccess: true,
          },
        },
      } as any); // NOTE: This is a workaround to get Amplify to work with TypeScript
      /* eslint-enable @typescript-eslint/no-explicit-any */

      setIsAmplifyConfigured(true);
    };

    configureAmplify();
  }, [isAmplifyConfigured]);

  useEffect(() => {
    if (isAmplifyConfigured) {
      const loadCurrentUser = async () => {
        try {
          const { username: amplify_username, userId, signInDetails } = await Auth.getCurrentUser();
          console.log('User already present: ', {
            username: amplify_username,
            userId,
            signInDetails,
          });
          dispatch({
            type: UserActionType.SET_USER,
            payload: {
              id: userId,
              username: amplify_username,
            },
          });
        } catch (error) {
          console.info('Could not find existing user:', error);
        }
        setIsLoading(false);
      };
      loadCurrentUser();
    }
  }, [isAmplifyConfigured, dispatch]);

  const signIn = async (username: string, password: string) => {
    await Auth.signIn({ username, password });
    const cognitoUser = await Auth.getCurrentUser();
    dispatch({
      type: UserActionType.SET_USER,
      payload: {
        id: cognitoUser.userId,
        username: cognitoUser.username,
      },
    });
  };

  const signOut = async () => {
    await Auth.signOut();
    dispatch({ type: UserActionType.CLEAR_USER });
  };

  const signUp = async (username: string, password: string, email: string) => {
    await Auth.signUp({
      username,
      password,
      options: {
        userAttributes: {
          email,
        },
        autoSignIn: true,
      },
    });
  };

  const confirmSignUp = async (username: string, confirmationCode: string) => {
    await Auth.confirmSignUp({ username, confirmationCode });
  };

  const resendSignUpCode = async (username: string) => {
    await Auth.resendSignUpCode({ username });
  };

  if (isLoading) {
    return null;
  }

  return (
    <UserContext.Provider
      value={{ user, dispatch, signIn, signOut, signUp, confirmSignUp, resendSignUpCode }}
    >
      {children}
    </UserContext.Provider>
  );
};
