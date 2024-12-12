import {
  QuizAction,
  QuizState,
  QuizRecordAction,
  QuizRecordState,
  QuizActionType,
  QuizRecordActionType,
} from 'features/quiz/types';

export const quizReducer = (quiz: QuizState, action: QuizAction): QuizState => {
  switch (action.type) {
    case QuizActionType.SET_QUIZ:
      return action.payload;
    default:
      return quiz;
  }
};

export const quizRecordReducer = (
  quizRecord: QuizRecordState,
  action: QuizRecordAction,
): QuizRecordState => {
  switch (action.type) {
    case QuizRecordActionType.SET_QUIZ_RECORD:
      return action.payload;
    default:
      return quizRecord;
  }
};
