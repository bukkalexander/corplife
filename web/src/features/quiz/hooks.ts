import React, { useContext, useReducer } from 'react';
import { QuizContext } from 'features/quiz/Context';
import { QuizState, QuizAction, QuizRecordState, QuizRecordAction } from 'features/quiz/types';
import { quizReducer, quizRecordReducer } from 'features/quiz/reducer';

export const useQuizReducer = () => {
  const initialState: QuizState = null;
  const [quiz, quizDispatch] = useReducer<React.Reducer<QuizState, QuizAction>>(
    quizReducer,
    initialState,
  );
  return { quiz, quizDispatch };
};

export const useQuizRecordReducer = () => {
  const initialState: QuizRecordState = null;
  const [quizRecord, quizRecordDispatch] = useReducer<
    React.Reducer<QuizRecordState, QuizRecordAction>
  >(quizRecordReducer, initialState);
  return { quizRecord, quizRecordDispatch };
};

export const useQuizContext = () => {
  const context = useContext(QuizContext);
  if (!context) {
    throw new Error('useQuizContext must be used within a QuizProvider');
  }
  return context;
};
