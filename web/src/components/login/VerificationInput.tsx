import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const VerificationCodeInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      label="Verification Code"
      id="verificationCode"
      type="text"
      value={value}
      onChange={onChange}
      required
    />
  );
};

export default VerificationCodeInput;
