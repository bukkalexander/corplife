import React from 'react';

interface LayoutProps {
  children: React.ReactNode;
}

const Container: React.FC<LayoutProps> = ({ children }) => {
  return <div className="min-h-screen flex flex-col bg-background-primary">{children}</div>;
};

const Header: React.FC<LayoutProps> = ({ children }) => {
  return (
    <header className="flex bg-background-secondary justify-end text-white">{children}</header>
  );
};

const Main: React.FC<LayoutProps> = ({ children }) => {
  return <main className="flex flex-col items-center m-2 bg-surface rounded-xl">{children}</main>;
};

export { Container, Header, Main };
