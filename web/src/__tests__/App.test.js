import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders the app correctly', () => {
  render(<App />);
  const linkElement = screen.getByText(/and save/i);
  expect(linkElement).toBeInTheDocument();
});
