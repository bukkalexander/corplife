import React, { ReactElement } from 'react';
import { Navigate } from 'react-router-dom';
import { useUserContext } from '@features/user';

interface ProtectedRouteProps {
  children?: ReactElement;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { user } = useUserContext();

  return user ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;
