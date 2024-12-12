import React, { useEffect } from 'react';
import Login from '@components/login/Login';
import { useNavigate } from 'react-router-dom';
import { useUserContext } from '@features/user';
import { Container, Header, Main } from '@components/common/Layout';
import UserBanner from '@components/common/UserBanner';

const LoginPage: React.FC = () => {
  const { user } = useUserContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (user) {
      navigate('/', { replace: true });
    }
  }, [user, navigate]);

  if (user) {
    return null;
  }

  return (
    <Container>
      <Header>
        <UserBanner />
      </Header>
      <Main>
        <Login />
      </Main>
    </Container>
  );
};

export default LoginPage;
