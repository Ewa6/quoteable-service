---
layout: default
title: Implement basic error handling when using the API
---

# Implement basic error handling when using the API

This tutorial demonstrates how to implement basic error handling when working with the Quoteable Service API. Proper error handling is important for creating robust applications that can gracefully manage unexpected situations.

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

- The Quoteable Service API uses standard HTTP status codes to indicate the success or failure of an API request.
- Implementing proper error handling improves the user experience and makes debugging easier.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Have a basic understanding of HTTP status codes.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Be familiar with making API requests using a programming language of your choice. This tutorial uses JavaScript in its examples.</li>
</ul>

## Implementing basic error handling

Use these steps to implement basic error handling when using the Quoteable Service API:

1. Make the API request.
2. Check the HTTP status code of the response.
3. If the status code indicates success (usually 200-299), process the response data.
4. If the status code indicates an error, handle it appropriately:
   - Parse the error message from the response body.
   - Log the error for debugging purposes.
   - Provide appropriate feedback to the user.

The following basic example uses JavaScript and the Fetch API:

```javascript
const BASE_URL = 'http://localhost:3000';

async function makeApiRequest(endpoint, method = 'GET', body = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json'
      }
    };

    if (body) {
      options.body = JSON.stringify(body);
    }

    const response = await fetch(`${BASE_URL}${endpoint}`, options);
    const text = await response.text();
    const data = text ? JSON.parse(text) : null;

    if (!response.ok) {
      const message = data?.message || response.statusText || 'Unknown error';
      throw new Error(`API error: ${response.status} - ${message}`);
    }

    return data;
  } catch (error) {
    console.error('Error making API request:', error);
    // Handle the error appropriately, for example, show an error message to the user.
    throw error;
  }
}

function showError(message) {
  const errorContainer = document.querySelector('[data-error-message]');

  if (errorContainer) {
    errorContainer.textContent = message;
  }
}

async function loadSubscriber() {
  try {
    const subscriber = await makeApiRequest('/subscribers/1');
    console.log('Subscriber data:', subscriber);
  } catch (error) {
    console.error('Failed to fetch subscriber:', error.message);
    showError('Failed to fetch subscriber data. Please try again later.');
  }
}

loadSubscriber();
```

## Common error scenarios and how to handle them

| Error | Cause | Handling |
| ----- | ----- | -------- |
| 400 Bad Request | Invalid JSON request body. | Check that the request body is valid JSON before sending it again. |
| 404 Not Found | The requested resource does not exist. | Check whether the ID or endpoint is correct. If you expect the resource to exist, it might have been deleted. Update your local data. |
| 500 Internal Server Error | Something went wrong on the server. | Log the error and retry the request after a short delay. If the error persists, contact API support. |

## Best practices

- Always check the HTTP status code before processing the response.
- Log errors for debugging, but be careful not to log sensitive information.
- Provide user-friendly error messages to your users.
- Implement retry logic for transient errors, such as network issues or 500 errors.
- Use a centralized error-handling mechanism in your application for consistency.

## What's next?

Now that you've learned about basic error handling:

- Implement comprehensive error handling in your application.
- Create a user-friendly way to display errors to your users.
- Set up logging for errors to help with debugging and monitoring.
- Consider implementing more advanced error handling, such as automatic retries for certain types of errors.
