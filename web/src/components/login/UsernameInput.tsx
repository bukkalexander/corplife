import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const UsernameInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      label="Username"
      id="username"
      type="text"
      value={value}
      onChange={onChange}
      required
    />
  );
};

export default UsernameInput;
