import React, { useEffect, useState } from 'react';
import { UserActionType, UserProviderProps } from '@features/user/types';
import { useUserReducer } from '@features/user/hooks';
import { UserContext } from '@features/user/Context';
import { loadUserFromLocalStorage, saveUserToLocalStorage } from '@features/user/persistence';

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
  const { user, dispatch } = useUserReducer();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadUser = async () => {
      const newUser = loadUserFromLocalStorage();
      dispatch({ type: UserActionType.SET_USER, payload: newUser });
      console.log(`newUser: ${newUser}`);
      setLoading(false);
    };
    if (loading) {
      loadUser();
    } else {
      saveUserToLocalStorage(user);
    }
  }, [user, loading, dispatch]);

  if (loading) {
    return <div>Loading user provider...</div>;
  }

  return <UserContext.Provider value={{ user, dispatch }}>{children}</UserContext.Provider>;
};
