---
layout: default
title: Update a subscriber's quote preferences
---

# Update a subscriber's quote preferences

This tutorial demonstrates how to update a subscriber's quote preferences using the Quoteable API. This process allows subscribers to change which types of quotes they want to receive.

<div class="tutorial-duration">
  <div class="icon-container">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="12 6 12 12 16 14"></polyline>
    </svg>
  </div>
  <div class="duration-text"><strong>Expected duration:</strong> Expect this tutorial to take about 10 minutes to complete.</div>
</div>

## Important notes

- You can update any combination of quote preferences (health, love, helping others) in a single request.
- If you only want to update one preference, only include that field in your request body.
- The API will return the entire updated subscriber object, including fields you didn't modify.
- At least one quote preference should be set to true to ensure the subscriber receives quotes.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose preferences you want to update.</li>
</ul>

## Update subscriber's quote preferences

To update a subscriber's quote preferences, you need to send a `PUT` request to the `/subscribers/{id}` endpoint with the updated preference information.

Follow these steps:

1. Open your API testing tool (e.g., Postman).
2. Create a new request with the following details:
    - METHOD: PUT
    - URL: `{{base_url}}/subscribers/{id}` (replace `{id}` with the actual subscriberId)
    - Headers:
        - Content-Type: application/json
        - Add any required authentication headers (if applicable).
    - Body (raw JSON):

    ```json
    {
      "healthQuote": true,
      "loveQuote": false,
      "helpPplQuote": true
    }
    ```

3. Send the request.

The successful request should return a status code `200 OK` with the updated subscriber object in the response body.

## Example

Request:

```js
PUT {{base_url}}/subscribers/1
Content-Type: application/json

{
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true
}
```

Response body:

```js
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "tony.stark@example.com",
  "mobile": "2125551234",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber id.
- `400 Bad Request`: Ensure your JSON is correctly formatted and contains valid boolean values.
- `401 Unauthorized`: Verify that you're including the correct authentication headers.

## What's next?

Now that you've learned how to update a subscriber's quote preferences, you can:

- pdate other subscriber details like delivery method or frequency.
- Retrieve the updated subscriber information to confirm changes.
- Use this method to build a preference management feature in your application.
