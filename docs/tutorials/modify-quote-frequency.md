---
layout: default
title: Modify a subscriber's quote frequency
---

# Modify a subscriber's quote frequency

This tutorial demonstrates how to update a subscriber's quote frequency using the Quoteable API. This process allows subscribers to choose how often they want to receive quotes.

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

- The quote frequency is represented by the `frequency` field in the subscriber object.
- `frequency` value of `1` represents daily delivery, `2` represents weekly delivery, and `3` represents monthly delivery.
- Changing the frequency doesn't affect the subscriber's quote preferences or delivery method.
- Ensure the frequency value is within the valid range (1-3).

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose quote frequency you want to modify.</li>
</ul>

## Modify subscriber's quote frequency

To modify a subscriber's quote frequency, you need to send a `PUT` request to the `/subscribers/{id}` endpoint with the updated `frequency` value.

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
      "frequency": 2
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
  "frequency": 2
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
  "frequency": 2
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber id.
- `400 Bad Request`: Ensure your JSON is correctly formatted and the frequency value is `1`, `2`, or `3`.
- `401 Unauthorized`: Verify that you're including the correct authentication headers.
- `422 Unprocessable Entity`: This may occur if the frequency value is outside the valid range. Ensure the frequency is set to `1` (daily), `2` (weekly), or `3` (monthly).

## What's next?

Now that you've learned how to modify a subscriber's quote frequency, you can:

- Update other subscriber details like quote preferences or delivery method.
- Retrieve the updated subscriber information to confirm changes.
- Implement a feature in your application allowing users to choose their preferred quote frequency.
- Consider adding a feature to your application that suggests changing the frequency based on user engagement (e.g., suggesting less frequent quotes if the user isn't opening daily emails).
