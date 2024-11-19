import globals from 'globals';
import react from 'eslint-plugin-react';
import reactHooks from 'eslint-plugin-react-hooks';
import typescriptPlugin from '@typescript-eslint/eslint-plugin';
import typescriptParser from '@typescript-eslint/parser';
import eslintRecommended from '@eslint/js';
import prettierConfig from 'eslint-config-prettier';
import eslintPluginUnusedImports from 'eslint-plugin-unused-imports';

const { configs: eslintRecommendedConfigs } = eslintRecommended;

export default [
  { ignores: ['dist', 'node_modules'] },
  {
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 'latest',
      globals: globals.browser,
      parser: typescriptParser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
        project: './tsconfig.json',
      },
    },
    settings: { react: { version: 'detect' } },
    plugins: {
      react,
      'react-hooks': reactHooks,
      '@typescript-eslint': typescriptPlugin,
      'unused-imports': eslintPluginUnusedImports,
    },
    rules: {
      ...eslintRecommendedConfigs.recommended.rules,
      ...react.configs.recommended.rules,
      ...react.configs['jsx-runtime'].rules,
      ...reactHooks.configs.recommended.rules,
      ...typescriptPlugin.configs.recommended.rules,
      'react/jsx-no-target-blank': 'off',
      'unused-imports/no-unused-imports': 'error', // This rule automatically removes unused imports
      'unused-imports/no-unused-vars': [
        'warn',
        {
          vars: 'all',
          varsIgnorePattern: '^_',
          args: 'after-used',
          argsIgnorePattern: '^_',
        },
      ],
      ...prettierConfig.rules,
    },
  },
];
