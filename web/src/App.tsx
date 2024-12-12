import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from '@pages/LoginPage';
import QuizPage from '@pages/QuizPage';
import { UserProvider, useUserContext } from '@features/user';
import ProtectedRoute from '@components/common/ProtectedRouter';
import { QuizProvider } from '@features/quiz/QuizProvider';
import QuizSelectionPage from '@pages/QuizSelectionPage';
import LeaderboardPage from '@pages/LeaderboardPage';

const AppContent: React.FC = () => {
  const { user } = useUserContext();
  console.log(`App: ${user}`);

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/quiz-selection"
          element={
            <ProtectedRoute>
              <QuizSelectionPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/quiz"
          element={
            <ProtectedRoute>
              <QuizPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/leaderboard"
          element={
            <ProtectedRoute>
              <LeaderboardPage />
            </ProtectedRoute>
          }
        />
        <Route path="/" element={<Navigate to={user ? '/quiz' : '/login'} replace />} />
      </Routes>
    </Router>
  );
};

const App: React.FC = () => {
  return (
    <UserProvider>
      <QuizProvider>
        <AppContent />
      </QuizProvider>
    </UserProvider>
  );
};

export default App;
