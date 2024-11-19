import React from 'react';
import TextBasedInput, { InputProps } from '@components/login/TextBasedInput';

const VerificationCodeInput: React.FC<InputProps> = ({ value, onChange }) => {
  return (
    <TextBasedInput
      id="verificationCode"
      type="text"
      value={value}
      onChange={onChange}
      required
      placeholder="Verification Code"
    />
  );
};

export default VerificationCodeInput;
