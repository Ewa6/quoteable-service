---
layout: default
title: Implement basic error handling when using the API
---

# Implement basic error handling when using the API

This tutorial demonstrates how to implement basic error handling when working with the Quoteable API. Proper error handling is crucial for creating robust applications that can gracefully manage unexpected situations.

<div class="tutorial-duration">
  <div class="icon-container">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="12 6 12 12 16 14"></polyline>
    </svg>
  </div>
  <div class="duration-text"><strong>Expected duration:</strong> Expect this tutorial to take about 20 minutes to complete.</div>
</div>

## Important notes

- The Quoteable API uses standard HTTP status codes to indicate the success or failure of an API request.
- Common error status codes include 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and 500 (Internal Server Error).
- The API returns error messages in JSON format, providing more details about the error.
- Implementing proper error handling improves the user experience and makes debugging easier.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Have a basic understanding of HTTP status codes.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Be familiar with making API requests using a programming language of your choice (we'll use JavaScript in our examples).</li>
</ul>

## Implementing basic error handling

Here's a step-by-step guide to implement basic error handling when using the Quoteable API:

1. Make the API request.
2. Check the HTTP status code of the response.
3. If the status code indicates success (usually 200-299), process the response data.
4. If the status code indicates an error, handle it appropriately:
   - Parse the error message from the response body.
   - Log the error for debugging purposes.
   - Provide appropriate feedback to the user.

Here's a basic example using JavaScript and the Fetch API:

```javascript
async function makeApiRequest(endpoint, method = 'GET', body = null) {
  try {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        // Add any necessary authentication headers
      },
      body: body ? JSON.stringify(body) : null
    });

    const data = await response.json();

    if (!response.ok) {
      // If the response status is not in the 200-299 range
      throw new Error(`API error: ${response.status} - ${data.message || 'Unknown error'}`);
    }

    return data;
  } catch (error) {
    console.error('Error making API request:', error);
    // Handle the error appropriately (e.g., show an error message to the user)
    throw error;
  }
}

// Usage example
try {
  const subscriber = await makeApiRequest('/subscribers/1');
  console.log('Subscriber data:', subscriber);
} catch (error) {
  console.error('Failed to fetch subscriber:', error.message);
  // Show error message to the user
  displayErrorToUser('Failed to fetch subscriber data. Please try again later.');
}
```

## Common error scenarios and how to handle them

- 400 Bad Request
    - Cause: Invalid input data
    - Handling: Check the error message for details about what's wrong with the input. Validate user input before sending requests.
- 401 Unauthorized
    - Cause: Invalid or missing authentication credentials
    - Handling: Check if the user is logged in. If not, prompt for login. If yes, the access token might be expired - try refreshing it.
- 404 Not Found
    - Cause: The requested resource doesn't exist
    - Handling: Check if the ID or endpoint is correct. If it should exist, it might have been deleted - update your local data.
- 422 Unprocessable Entity
    - Cause: The request was well-formed but contains semantic errors
    - Handling: Similar to 400, but often related to business logic. Check the error message for details and adjust your request accordingly.
- 500 Internal Server Error
    - Cause: Something went wrong on the server
    - Handling: This is not your fault. Log the error, and retry the request after a short delay. If it persists, contact the API support.

## Best practices

- Always check the HTTP status code before processing the response.
- Log errors for debugging, but be careful not to log sensitive information.
- Provide user-friendly error messages to your users.
- Implement retry logic for transient errors (like network issues or 500 errors).
- Use a centralized error handling mechanism in your application for consistency.

## What's next?

Now that you've learned about basic error handling:

- Implement comprehensive error handling in your application.
- Create a user-friendly way to display errors to your users.
- Set up logging for errors to help with debugging and monitoring.
- Consider implementing more advanced error handling, such as automatic retries for certain types of errors.