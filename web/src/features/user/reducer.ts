import { UserAction, UserActionType, UserState } from '@features/user/types';

export const userReducer = (user: UserState, action: UserAction): UserState => {
  switch (action.type) {
    case UserActionType.SET_USER:
      return action.payload;
    case UserActionType.CLEAR_USER:
      return null;
    default:
      return user;
  }
};
