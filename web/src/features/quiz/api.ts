import { fetchData } from '@services/api';
import { Quiz, Question, QuizRecord } from '@features/quiz/types';
import { fetchConfig } from '@features/config';
import { z } from 'zod';

// TODO: returns a question read for now, since we don't have quiz in the backend api yet
export const readQuiz = async (quizId: string): Promise<Quiz> => {
  const config = await fetchConfig();
  const fetchQuestionsUrl = `${config.apiUrl}/questions`;

  const ApiQuestionSchema = z.object({
    text: z.string(),
    answers: z.array(z.string()),
    correctAnswer: z.number(),
  });

  const ApiQuestionArraySchema = z.array(ApiQuestionSchema);
  type ApiQuestionArray = z.infer<typeof ApiQuestionArraySchema>;
  const apiQuestionArray = await fetchData<ApiQuestionArray>(
    fetchQuestionsUrl,
    ApiQuestionArraySchema,
  );

  const questions: Question[] = apiQuestionArray.map((apiQuestion) => ({
    id: quizId,
    text: apiQuestion.text,
    answers: apiQuestion.answers.map((answer) => ({ text: answer })),
    correctAnswerIndex: apiQuestion.correctAnswer,
  }));

  const quiz = {
    id: quizId,
    ownerId: '1',
    title: 'Quiz Title',
    questions: questions,
  };
  return quiz;
};

// TODO: returns a dummy create for now, since we don't have quizRecord in the backend api yet
export const createQuizRecord = async (quizId: string, userId: string): Promise<QuizRecord> => {
  const config = await fetchConfig();
  if (!config) {
    throw new Error('Configuration could not be loaded');
  }
  const quizRecord = {
    id: '1337',
    quizId: quizId,
    userId: userId,
    questionRecords: [
      {
        questionId: '1',
        selectedAnswerIndex: 0,
      },
      {
        questionId: '2',
        selectedAnswerIndex: 1,
      },
    ],
  };
  return quizRecord;
};
