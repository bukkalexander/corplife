import React from 'react';
import Leaderboard from '@components/leaderboard/Leaderboard';
import { Container, Header, Main } from '@components/common/Layout';
import UserBanner from '@components/common/UserBanner';

const LeaderboardPage: React.FC = () => {
  return (
    <Container>
      <Header>
        <UserBanner />
      </Header>
      <Main>
        <Leaderboard />
      </Main>
    </Container>
  );
};

export default LeaderboardPage;
