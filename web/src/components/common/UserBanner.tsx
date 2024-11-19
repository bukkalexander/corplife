import React from 'react';
import Button from '@components/common/Button';
import { UserActionType, useUserContext } from '@features/user';
import { signOut } from '@aws-amplify/auth';

const UserBanner: React.FC = () => {
  const { user, dispatch: dispatchUser } = useUserContext();

  const handleLogout = async () => {
    if (!user) return;
    try {
      await signOut();
      dispatchUser({ type: UserActionType.CLEAR_USER });
      console.log(`Logged out user with username: ${user.username}`);
    } catch (error) {
      console.error(`Logout failed for user with username: ${user.username}`, error);
    }
  };

  if (!user) return null;
  return (
    <div className="flex items-center p-2 gap-4">
      <span>{user.username}</span>
      <Button onClick={handleLogout}>Logout</Button>
    </div>
  );
};

export default UserBanner;
