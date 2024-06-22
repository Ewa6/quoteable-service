---
layout: default
title: Your Page Title
---

# Update a subscriber's email or mobile

This tutorial demonstrates how to update a subscriber's email address or mobile number using the Quoteable API. This process is useful when subscribers need to change their contact information.

{% include tutorial-duration.html duration="10 minutes" %}

{% include important-notes.html content="
<ul>
  <li>You can update either the email, mobile, or both in a single request.</li>
  <li>If you only want to update one field, only include that field in your request body.</li>
  <li>The API will return the entire updated subscriber object, including fields you didn't modify.</li>
  <li>Ensure that the new email address is valid and the new mobile number is in the correct format.</li>
</ul>
" %}

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the `id` of the subscriber you want to update.</li>
</ul>

## Update subscriber information

To update a subscriber's email or mobile number, you need to send a `PUT` request to the `/subscribers/{id}` endpoint with the updated information.

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
      "email": "new.email@example.com",
      "mobile": "9876543210"
    }
    ```

3. Send the request.

The successful request should return a status code `200 OK` with the updated subscriber object in the response body.

## Example

Request:

```http
PUT {{base_url}}/subscribers/1
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
