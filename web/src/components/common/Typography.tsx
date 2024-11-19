import React from 'react';

interface TypographyProps {
  children: React.ReactNode;
}

const H1: React.FC<TypographyProps> = ({ children }) => {
  return <h1 className="text-3xl font-bold mb-3">{children}</h1>;
};

const H2: React.FC<TypographyProps> = ({ children }) => {
  return <h2 className="text-2xl font-semibold mb-2">{children}</h2>;
};

const H3: React.FC<TypographyProps> = ({ children }) => {
  return <h3 className="text-xl font-medium mb-1">{children}</h3>;
};

const P: React.FC<TypographyProps> = ({ children }) => {
  return <p className="mb-4">{children}</p>;
};

export { H1, H2, H3, P };
