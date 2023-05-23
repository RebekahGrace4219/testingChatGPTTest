// Prompt: Can you generate a JEST test for the React component you made earlier?
//Certainly! Here's an example of how you can write a JEST test for the React component:

import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';

describe('App', () => {
  test('Clicking the "Git" button redirects to the GitHub page', () => {
    render(
      <Router>
        <App />
      </Router>
    );

    // Find the "Git" button
    const gitButton = screen.getByRole('button', { name: 'Git' });

    // Simulate a click on the "Git" button
    userEvent.click(gitButton);

    // Check if the URL has changed to the GitHub page
    expect(window.location.href).toBe('https://github.com/RebekahGrace4219');
  });
});

/*
Make sure to install the necessary dependencies (`@testing-library/react`, `@testing-library/user-event`, `react-router-dom`) before running the test.
This test verifies that clicking the "Git" button redirects the user to the correct GitHub page. You can further enhance the test suite by adding more tests to cover different functionalities and edge cases of your React component.*/
