import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const EmailInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      label="Email"
      id="email"
      type="email"
      value={value}
      onChange={onChange}
      required
    />
  );
};

export default EmailInput;
