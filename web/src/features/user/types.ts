import { Dispatch, ReactNode } from 'react';
import { z } from 'zod';

export const UserSchema = z.object({
  id: z.string(),
  username: z.string(),
});

export const UserStateSchema = UserSchema.nullable();

export type User = z.infer<typeof UserSchema>;
export type UserState = z.infer<typeof UserStateSchema>;

export interface UserProviderProps {
  children: ReactNode;
}

export interface UserContextType {
  user: UserState;
  dispatch: Dispatch<UserAction>;
  signIn: (username: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
  signUp: (username: string, password: string, email: string) => Promise<void>;
  confirmSignUp: (username: string, code: string) => Promise<void>;
  resendSignUpCode: (username: string) => Promise<void>;
}

export enum UserActionType {
  SET_USER = 'SET_USER',
  CLEAR_USER = 'CLEAR_USER',
}

export type UserAction =
  | { type: UserActionType.SET_USER; payload: UserState }
  | { type: UserActionType.CLEAR_USER };
