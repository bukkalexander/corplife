import React from 'react';

interface ButtonProps {
  onClick?: () => void;
  children: React.ReactNode;
  disabled?: boolean;
  type?: 'button' | 'submit';
  variant?: 'primary' | 'secondary';
}

const Button: React.FC<ButtonProps> = ({
  onClick,
  children,
  disabled = false,
  type = 'button',
  variant = 'primary',
}) => {
  const baseClass = 'p-2 rounded text-text-secondary';
  const variantClass =
    variant === 'primary'
      ? 'bg-button-bg-primary hover:bg-button-bg-primary-hover'
      : 'bg-button-bg-secondary hover:bg-button-bg-secondary-hover';
  const disabledClass = 'disabled:bg-button-bg-disabled disabled:cursor-not-allowed';

  const classNames = `${baseClass} ${variantClass} ${disabledClass}`;

  return (
    <button onClick={onClick} disabled={disabled} type={type} className={classNames}>
      {children}
    </button>
  );
};

export default Button;
