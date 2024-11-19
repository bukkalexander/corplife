import React from 'react';

interface ButtonProps {
  onClick?: () => void;
  children: React.ReactNode;
  disabled?: boolean;
  type?: 'button' | 'submit' | 'reset';
}

const Button: React.FC<ButtonProps> = ({
  onClick,
  children,
  disabled = false,
  type = 'button',
}) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      type={type}
      className="bg-primary text-white p-2 rounded hover:bg-primary-hover disabled:bg-gray-400"
    >
      {children}
    </button>
  );
};

export default Button;
