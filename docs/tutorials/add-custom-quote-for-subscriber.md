---
layout: default
title: Add a custom quote for a subscriber
---

# Add a custom quote for a subscriber

This tutorial demonstrates how to add a custom quote for a subscriber using the Quoteable API. This process allows subscribers to include their own personalized quotes in their quote rotation.

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

- Adding a custom quote involves setting the `customQuote` field to `true` and providing the quote text in the `customQuoteText` field.
- Custom quotes are subject to review before we add them to the subscriber's rotation.
- Adding a custom quote doesn't affect the subscriber's other quote preferences or delivery settings.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber for whom you want to add a custom quote.</li>
</ul>

## Add a custom quote for a subscriber

To add a custom quote for a subscriber, you need to send a `PUT` request to the `/subscribers/{id}` endpoint with the `customQuote` set to `true` and the `customQuoteText` containing the quote.

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
      "customQuote": true,
      "customQuoteText": "Your custom quote goes here."
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
  "customQuote": true,
  "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi"
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
  "frequency": 3,
  "customQuote": true,
  "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi"
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct `subscriberId`.
- `400 Bad Request`: Ensure your JSON is correctly formatted and includes both `customQuote` and `customQuoteText` fields.
- `401 Unauthorized`: Verify that you're including the correct authentication headers.
- `422 Unprocessable Entity`: This may occur if the custom quote text is empty or exceeds the maximum allowed length. Ensure the quote text is not empty and within the allowed character limit.

## What's next?

Now that you've learned how to add a custom quote for a subscriber, you can:

- Implement a feature in your application for users to submit their own quotes.
- Create a moderation system for reviewing and approving custom quotes before they're added to the rotation.
- Develop a feature to display a subscriber's custom quote alongside quotes from the standard categories.
- Consider adding functionality to edit or delete custom quotes.