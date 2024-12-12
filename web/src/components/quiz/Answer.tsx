import React from 'react';

interface AnswerProps {
  index: number;
  groupId: string;
  selectedAnswerIndex: number | null;
  correctAnswerIndex: number;
  isSubmitted: boolean;
  onSelected: (event: React.ChangeEvent<HTMLInputElement>) => void;
  children: React.ReactNode;
}

const Answer: React.FC<AnswerProps> = ({
  index,
  groupId,
  selectedAnswerIndex,
  correctAnswerIndex,
  isSubmitted,
  onSelected,
  children,
}) => {
  const isSelected = selectedAnswerIndex === index;
  const isCorrectAnswer = index === correctAnswerIndex;

  const getTextColorClass = (): string | null => {
    const successColorClass = 'text-green-500';
    const failureColorClass = 'text-red-500';
    if (isSubmitted) {
      if (isCorrectAnswer) {
        return successColorClass;
      } else if (isSelected) {
        return failureColorClass;
      }
    }
    return null;
  };
  const textColorClass = getTextColorClass();
  const classNames = `
    flex border rounded w-full
    ${textColorClass ? textColorClass : ''}
  `;

  const answerRadioInputId = `answerRadioInput${index}`;
  return (
    <div key={index} className={classNames}>
      <input
        type="radio"
        name={groupId}
        id={answerRadioInputId}
        value={index}
        checked={isSelected}
        disabled={isSubmitted}
        onChange={onSelected}
        className="flex m-2"
      />
      <label htmlFor={answerRadioInputId} className="w-full py-2">
        {children}
      </label>
    </div>
  );
};

export default Answer;
