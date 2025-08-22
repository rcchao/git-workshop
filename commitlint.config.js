module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [2, 'always', [
      'calculator',
      'utils',
      'main',
    ]],
  },
};
