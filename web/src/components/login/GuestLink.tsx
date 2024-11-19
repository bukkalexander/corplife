import React from 'react';

interface GuestLinkProps {
  onClick: () => void;
}

const GuestLink: React.FC<GuestLinkProps> = ({ onClick }) => {
  return (
    <a
      href="#continue-as-guest"
      onClick={(e) => {
        e.preventDefault();
        onClick();
      }}
      className="text-blue-500 hover:text-blue-700 underline"
    >
      Continue as Guest
    </a>
  );
};

export default GuestLink;
