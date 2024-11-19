import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const PasswordInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      label="Password"
      id="password"
      type="password"
      value={value}
      onChange={onChange}
      required
    />
  );
};

export default PasswordInput;
