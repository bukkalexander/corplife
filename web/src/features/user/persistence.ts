import { loadFromLocalStorage, saveToLocalStorage } from '@services/persistence';
import { UserState, UserStateSchema } from '@features/user/types';
import { LOCAL_STORAGE_USER_KEY } from '@/constants';

export const loadUserFromLocalStorage = (): UserState => {
  return loadFromLocalStorage<UserState>(LOCAL_STORAGE_USER_KEY, UserStateSchema);
};

export const saveUserToLocalStorage = (user: UserState) => {
  saveToLocalStorage<UserState>(LOCAL_STORAGE_USER_KEY, user, UserStateSchema);
};
