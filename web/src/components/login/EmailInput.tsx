import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const EmailInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      id="email"
      type="email"
      value={value}
      onChange={onChange}
      required
      placeholder="Email"
    />
  );
};

export default EmailInput;
