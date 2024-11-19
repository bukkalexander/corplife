/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'button-bg-primary': 'var(--color-button-bg-primary)',
        'button-bg-primary-hover': 'var(--color-button-bg-primary-hover)',
        'button-bg-secondary': 'var(--color-button-bg-secondary)',
        'button-bg-secondary-hover': 'var(--color-button-bg-secondary-hover)',
        'button-bg-disabled': 'var(--color-button-bg-disabled)',
        'bg-primary': 'var(--color-bg-primary)',
        'bg-secondary': 'var(--color-bg-secondary)',
        'content-bg-primary': 'var(--color-content-bg-primary)',
        'text-primary': 'var(--color-text-primary)',
        'text-secondary': 'var(--color-text-secondary)',
        link: 'var(--color-link)',
        'link-hover': 'var(--color-link-hover)',
      },
    },
  },
  plugins: [],
};
