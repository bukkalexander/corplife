import React from 'react';

export interface InputProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

interface TextBasedInputProps extends InputProps {
  label?: string;
  id: string;
  type: string;
  required?: boolean;
  className?: string;
  placeholder?: string;
}

const TextBasedInput: React.FC<TextBasedInputProps> = ({
  label,
  id,
  type,
  value,
  onChange,
  required = false,
  className = 'p-2 border rounded-md shadow-sm',
  placeholder = '',
}) => {
  return (
    <div className="flex flex-col">
      {label && <label htmlFor={id}>{label}</label>}
      <input
        type={type}
        id={id}
        value={value}
        onChange={onChange}
        required={required}
        className={className}
        placeholder={placeholder}
      />
    </div>
  );
};

export default TextBasedInput;
