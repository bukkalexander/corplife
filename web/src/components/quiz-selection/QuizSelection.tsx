import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { H1, P } from '@components/common/Typography';
import { Content } from '@components/common/Layout';
import Button from '@components/common/Button';
import { QuizActionType, QuizRecordActionType, useQuizContext } from '@features/quiz';
import { readQuiz, createQuizRecord } from '@features/quiz/api';
import { useUserContext } from '@features/user';
import { ClipLoader } from 'react-spinners';

const QuizSelectionPage: React.FC = () => {
  const navigate = useNavigate();
  const { user } = useUserContext();
  const { quizDispatch, quizRecordDispatch } = useQuizContext();
  const [isQuizStarted, setIsQuizStarted] = useState(false);

  const quizId = '0';

  useEffect(() => {
    const startQuiz = async () => {
      if (!user) return;
      if (!isQuizStarted) return;

      const quiz = await readQuiz(quizId);
      quizDispatch({ type: QuizActionType.SET_QUIZ, payload: quiz });

      const quizRecord = await createQuizRecord(quizId, user.id);
      quizRecordDispatch({ type: QuizRecordActionType.SET_QUIZ_RECORD, payload: quizRecord });

      navigate(`/quiz`);
    };
    startQuiz();
  }, [user, isQuizStarted, navigate, quizDispatch, quizRecordDispatch]);

  const handleStartQuiz = () => {
    setIsQuizStarted(true);
  };

  if (isQuizStarted) {
    return (
      <Content>
        <H1>Starting Quiz...</H1>
        <ClipLoader />
        <P>Fetching quiz data...</P>
      </Content>
    );
  }
  return (
    <Content>
      <H1>Select a Quiz</H1>
      <P>
        TODO: implement quiz selection logic. Just press the &quot;start&quot; button to start a
        Quiz.
      </P>
      <Button onClick={handleStartQuiz}>Start</Button>
    </Content>
  );
};

export default QuizSelectionPage;
