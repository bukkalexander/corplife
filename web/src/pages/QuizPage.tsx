import React from 'react';
import Quiz from '@components/quiz/Quiz';
import UserBanner from '@components/common/UserBanner';
import { Container, Header, Main } from '@components/common/Layout';

const QuizPage: React.FC = () => {
  return (
    <Container>
      <Header>
        <UserBanner />
      </Header>
      <Main>
        <Quiz />
      </Main>
    </Container>
  );
};

export default QuizPage;
