import { createContext } from 'react';
import { QuizContextType } from '@features/quiz/types';

export const QuizContext = createContext<QuizContextType | undefined>(undefined);
