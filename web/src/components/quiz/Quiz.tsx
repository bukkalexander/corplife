import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { H1, H2, P } from '@components/common/Typography';
import Form from '@components/common/Form';
import Answer from '@components/quiz/Answer';
import Button from '@components/common/Button';
import { useQuizContext } from '@features/quiz';
import { Content } from '@components/common/Layout';

const Quiz: React.FC = () => {
  const navigate = useNavigate();

  const { quiz } = useQuizContext();
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswerIndex, setSelectedAnswerIndex] = useState<number | null>(null);
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false);
  const [isQuizCompleted, setIsQuizCompleted] = useState(false);

  useEffect(() => {
    if (!quiz) {
      navigate('/quiz-selection');
    }
  }, [quiz, navigate]);

  useEffect(() => {
    if (isQuizCompleted) {
      navigate('/leaderboard');
    }
  }, [isQuizCompleted, navigate]);

  if (isQuizCompleted) {
    return null;
  }

  if (!quiz) {
    return <P>No quiz selected...</P>;
  }
  const currentQuestion = quiz.questions[currentQuestionIndex];

  const handleSubmitAnswer = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (selectedAnswerIndex === currentQuestion.correctAnswerIndex) {
      // TODO: post quizRecord update to server
    }
    setIsAnswerSubmitted(true);
  };

  const handleAnswerSelected = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedAnswerIndex(Number(event.target.value));
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex < quiz.questions.length - 1) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
      setSelectedAnswerIndex(null);
      setIsAnswerSubmitted(false);
    } else {
      setIsQuizCompleted(true);
    }
  };

  const questionCountText = `Question ${currentQuestionIndex + 1} / ${quiz.questions.length}`;
  const questionText = `${quiz.questions[0].text}`;
  const isAnswerSelected = selectedAnswerIndex !== null;
  return (
    <Content>
      <H1>{quiz.title}</H1>
      <H2>{questionCountText}</H2>
      <P>{questionText}</P>
      <Form onSubmit={handleSubmitAnswer}>
        {currentQuestion.answers.map((answer, index) => (
          <Answer
          key={index}
          index={index}
          groupId="answers"
          selectedAnswerIndex={selectedAnswerIndex}
          correctAnswerIndex={currentQuestion.correctAnswerIndex}
          isSubmitted={isAnswerSubmitted}
          onSelected={handleAnswerSelected}
          >
            {answer.text}
          </Answer>
        ))}
        {isAnswerSubmitted ? (
          <Button onClick={handleNextQuestion}>Next</Button>
        ) : (
          <Button type="submit" disabled={!isAnswerSelected}>
            Submit
          </Button>
        )}
      </Form>
    </Content>
  );
};

export default Quiz;
