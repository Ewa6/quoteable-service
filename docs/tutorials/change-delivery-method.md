---
layout: default
title: Change a subscriber's quote delivery method
---

# Change a subscriber's quote delivery method

This tutorial demonstrates how to update a subscriber's quote delivery method using the Quoteable API. This process allows subscribers to choose whether they want to receive quotes via email or text message.

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

- The delivery method is represented by the `deliverTo` field in the subscriber object.
- `deliverTo` value of 1 represents email delivery, while 2 represents text message delivery.
- Ensure the subscriber has a valid email address for email delivery or a valid mobile number for text message delivery.
- Changing the delivery method doesn't affect the subscriber's quote preferences or frequency.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose delivery method you want to change.</li>
</ul>

## Change subscriber's quote delivery method

To change a subscriber's quote delivery method, you need to send a `PUT` request to the `/subscribers/{id}` endpoint with the updated `deliverTo` value.

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
      "deliverTo": 2
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
  "deliverTo": 2
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
  "deliverTo": 2,
  "frequency": 3
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber id.
- `400 Bad Request`: Ensure your JSON is correctly formatted and the deliverTo value is either 1 or 2.
- `401 Unauthorized`: Verify that you're including the correct authentication headers.
- `422 Unprocessable Entity`: This may occur if trying to set delivery to text message (2) when no mobile number is provided. Ensure the subscriber has a mobile number if selecting text message delivery.

## What's next?

Now that you've learned how to change a subscriber's quote delivery method, you can:

- Update other subscriber details like quote preferences or delivery frequency.
- Retrieve the updated subscriber information to confirm changes.
- Implement a feature in your application allowing users to toggle between email and text message delivery.
- Consider adding validation in your application to ensure the appropriate contact information (email or mobile) is available before changing the delivery method.
