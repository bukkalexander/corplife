import React from 'react';
import { Container, Main } from '@components/common/Layout';
import QuizSelection from '@components/quiz-selection/QuizSelection';

const QuizSelectionPage: React.FC = () => {
  return (
    <Container>
      <Main>
        <QuizSelection />
      </Main>
    </Container>
  );
};

export default QuizSelectionPage;
