import { Dispatch, ReactNode } from 'react';
import { z } from 'zod';

export const AnswerSchema = z.object({
  text: z.string(),
});

export const QuestionSchema = z.object({
  id: z.string(),
  text: z.string(),
  answers: z.array(AnswerSchema),
  correctAnswerIndex: z.number(),
});

export const QuizSchema = z.object({
  id: z.string(),
  ownerId: z.string(),
  title: z.string(),
  questions: z.array(QuestionSchema),
});

export const QuizStateSchema = QuizSchema.nullable();

export const QuestionRecordSchema = z.object({
  questionId: z.string(),
  selectedAnswerIndex: z.number(),
});

export const QuizRecordSchema = z.object({
  id: z.string(),
  quizId: z.string(),
  userId: z.string(),
  questionRecords: z.array(QuestionRecordSchema),
});

export const QuizRecordStateSchema = QuizRecordSchema.nullable();

// Infer TypeScript types from Zod schemas
export type Answer = z.infer<typeof AnswerSchema>;
export type Question = z.infer<typeof QuestionSchema>;
export type Quiz = z.infer<typeof QuizSchema>;
export type QuestionRecord = z.infer<typeof QuestionRecordSchema>;
export type QuizRecord = z.infer<typeof QuizRecordSchema>;

export type QuizState = z.infer<typeof QuizStateSchema>;
export type QuizRecordState = z.infer<typeof QuizRecordStateSchema>;

export enum QuizActionType {
  SET_QUIZ = 'SET_QUIZ',
}
export enum QuizRecordActionType {
  SET_QUIZ_RECORD = 'SET_QUIZ_RECORD',
}
export type QuizAction = { type: QuizActionType.SET_QUIZ; payload: QuizState };

export type QuizRecordAction = {
  type: QuizRecordActionType.SET_QUIZ_RECORD;
  payload: QuizRecordState;
};

export interface QuizContextType {
  quiz: QuizState;
  quizRecord: QuizRecordState;
  quizDispatch: Dispatch<QuizAction>;
  quizRecordDispatch: Dispatch<QuizRecordAction>;
}

export interface QuizProviderProps {
  children: ReactNode;
}
