import React, { useContext, useReducer } from 'react';
import { UserContext } from '@/features/user/Context';
import { UserState, UserAction } from '@/features/user/types';
import { userReducer } from '@/features/user/reducer';

export const useUserReducer = () => {
  const initialState: UserState = null;
  const [user, dispatch] = useReducer<React.Reducer<UserState, UserAction>>(
    userReducer,
    initialState,
  );
  return { user, dispatch };
};

export const useUserContext = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUserContext must be used within a UserProvider');
  }
  return context;
};
