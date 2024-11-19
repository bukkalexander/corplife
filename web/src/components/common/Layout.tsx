import React from 'react';

interface LayoutProps {
  children: React.ReactNode;
}

const Container: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen  bg-bg-primary text-text-primary">{children}</div>
  );
};

const Header: React.FC<LayoutProps> = ({ children }) => {
  return (
    <header className="flex bg-bg-secondary justify-end text-text-secondary">{children}</header>
  );
};

const Main: React.FC<LayoutProps> = ({ children }) => {
  return <main className="flex flex-col items-center w-full p-8">{children}</main>;
};

const Content: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex flex-col items-center gap-4 w-full max-w-[500px] min-w-[300px] bg-content-bg-primary rounded-lg shadow-lg p-4">
      {children}
    </div>
  );
};

export { Container, Header, Main, Content };
