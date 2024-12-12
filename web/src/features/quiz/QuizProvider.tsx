import React, { useEffect, useState } from 'react';
import {
  loadQuizFromLocalStorage,
  saveQuizToLocalStorage,
  loadQuizRecordFromLocalStorage,
  saveQuizRecordToLocalStorage,
} from '@features/quiz/persistence';
import { QuizProviderProps, QuizActionType, QuizRecordActionType } from '@features/quiz/types';
import { QuizContext } from '@features/quiz/Context';
import { useQuizRecordReducer, useQuizReducer } from '@features/quiz/hooks';

export const QuizProvider: React.FC<QuizProviderProps> = ({ children }) => {
  const { quiz, quizDispatch } = useQuizReducer();
  const { quizRecord, quizRecordDispatch } = useQuizRecordReducer();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadQuizData = async () => {
      const newQuiz = loadQuizFromLocalStorage();
      const newQuizRecord = loadQuizRecordFromLocalStorage();
      quizDispatch({ type: QuizActionType.SET_QUIZ, payload: newQuiz });
      quizRecordDispatch({
        type: QuizRecordActionType.SET_QUIZ_RECORD,
        payload: newQuizRecord,
      });
      setLoading(false);
    };
    if (loading) {
      loadQuizData();
    } else {
      saveQuizToLocalStorage(quiz);
      saveQuizRecordToLocalStorage(quizRecord);
    }
  }, [quiz, quizRecord, loading, quizDispatch, quizRecordDispatch]);

  if (loading) {
    return null;
  }

  return (
    <QuizContext.Provider value={{ quiz, quizRecord, quizDispatch, quizRecordDispatch }}>
      {children}
    </QuizContext.Provider>
  );
};
