import { loadFromLocalStorage, saveToLocalStorage } from '@/services/persistence';
import {
  QuizState,
  QuizRecordState,
  QuizStateSchema,
  QuizRecordStateSchema,
} from '@/features/quiz/types';
import { LOCAL_STORAGE_QUIZ_KEY, LOCAL_STORAGE_QUIZ_RECORD_KEY } from '@/constants';

export const loadQuizFromLocalStorage = (): QuizState => {
  return loadFromLocalStorage<QuizState>(LOCAL_STORAGE_QUIZ_KEY, QuizStateSchema);
};

export const saveQuizToLocalStorage = (quiz: QuizState) => {
  saveToLocalStorage<QuizState>(LOCAL_STORAGE_QUIZ_KEY, quiz, QuizStateSchema);
};

export const loadQuizRecordFromLocalStorage = (): QuizRecordState => {
  return loadFromLocalStorage<QuizRecordState>(
    LOCAL_STORAGE_QUIZ_RECORD_KEY,
    QuizRecordStateSchema,
  );
};

export const saveQuizRecordToLocalStorage = (quizRecord: QuizRecordState) => {
  saveToLocalStorage<QuizRecordState>(
    LOCAL_STORAGE_QUIZ_RECORD_KEY,
    quizRecord,
    QuizRecordStateSchema,
  );
};
