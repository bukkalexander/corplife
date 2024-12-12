import React, { ReactNode, FormEvent } from 'react';

interface FormProps {
  children: ReactNode;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

const Form: React.FC<FormProps> = ({ children, onSubmit }) => {
  return (
    <form className="flex flex-col w-full gap-2" onSubmit={onSubmit}>
      {children}
    </form>
  );
};

export default Form;
