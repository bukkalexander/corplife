import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const PasswordInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      id="password"
      type="password"
      value={value}
      onChange={onChange}
      required
      placeholder="Password"
    />
  );
};

export default PasswordInput;
