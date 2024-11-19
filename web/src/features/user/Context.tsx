import { createContext } from 'react';
import { UserContextType } from 'features/user/types';

export const UserContext = createContext<UserContextType | undefined>(undefined);
