import React from 'react';

export interface InputProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

interface TextBasedInputProps extends InputProps {
  label: string;
  id: string;
  type: string;
  required?: boolean;
  className?: string;
}

const TextBasedInput: React.FC<TextBasedInputProps> = ({
  label,
  id,
  type,
  value,
  onChange,
  required = false,
  className = 'mt-1 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
}) => {
  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input
        type={type}
        id={id}
        value={value}
        onChange={onChange}
        required={required}
        className={className}
      />
    </>
  );
};

export default TextBasedInput;
