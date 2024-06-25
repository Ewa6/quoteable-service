---
layout: default
title: Your Page Title
---

# Update a subscriber's email or mobile

This tutorial demonstrates how to update a subscriber's email address or mobile number using the Quoteable API. This process is useful when subscribers need to change their contact information.

<div class="tutorial-duration">
  <div class="icon-container">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="12 6 12 12 16 14"></polyline>
    </svg>
  </div>
  <div class="duration-text"><strong>Expected duration:</strong> Expect this tutorial to take about 15 minutes to complete.</div>
</div>

## Important notes

- You can update either the email, mobile, or both in a single request.
- If you only want to update one field, only include that field in your request body.
- The API will return the entire updated subscriber object, including fields you didn't modify.
- Ensure that the new email address is valid and the new mobile number is in the correct format.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber you want to update.</li>
</ul>

## Update subscriber information

To update a subscriber's email or mobile number, you need to send a `PATCH` request to the `/subscribers/{id}` endpoint with the updated information.

Follow these steps:

1. Open your API testing tool (e.g., Postman).
2. Create a new request with the following details:
    - METHOD: PATCH
    - URL: `{{base_url}}/subscribers/{id}` (replace `{id}` with the actual subscriberId)
    - Headers:
        - Content-Type: application/json
        - Add any required authentication headers (if applicable).
    - Body (raw JSON):

    ```json
    {
      "email": "new.email@example.com",
      "mobile": "9876543210"
    }
    ```

3. Send the request.

The successful request should return a status code `200 OK` with the updated subscriber object in the response body.

## Example

Request:

```http
PATCH {{base_url}}/subscribers/1
Content-Type: application/json

{
  "email": "tony.stark.new@example.com",
  "mobile": "2125559999"
}
```

Response body:

```js
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "tony.stark.new@example.com",
  "mobile": "2125559999",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3
}
```

## Error Handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber id.
- `400 Bad Request`: Ensure your JSON is correctly formatted and contains valid data.
- `401 Unauthorized`: Verify that you're including the correct authentication headers.

## What's Next?

Now that you've learned how to update a subscriber's contact information, you can:

- Update other subscriber details like name or quote preferences.
- Retrieve the updated subscriber information to confirm changes.
- Use this method to build a user profile update feature in your application.
