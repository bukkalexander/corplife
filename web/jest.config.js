export default {
    testEnvironment: 'jsdom',
    setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
    moduleNameMapper: {
      '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
      '\\.(svg|jpg|jpeg|png)$': '<rootDir>/__mocks__/fileMock.js', // Mock image imports
    },
  };
  
  