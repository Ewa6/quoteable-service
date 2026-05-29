---
layout: default
title: Add a custom quote for a subscriber
---

# Add a custom quote for a subscriber

This tutorial demonstrates how to add a custom quote for a subscriber using the Quoteable Service API. This process lets subscribers include their own personalized quotes in their quote rotation.

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
- In this mock API, custom quotes are added directly to the quote record. Add review or moderation in your own application if you need it.
- Adding a custom quote doesn't affect the subscriber's other quote preferences or delivery settings.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have a tool such as Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber for whom you want to add a custom quote.</li>
</ul>

## Add a custom quote for a subscriber

To add a custom quote for a subscriber, send a `PATCH` request to the `/quotes/{id}` endpoint with `customQuote` set to `true` and `customQuoteText` containing the quote.

For endpoint details, see [Update a quote](../api/quotes-patch-quote.html).

Follow these steps:

1. Open your API testing tool, such as Postman.
2. Create a new request with the following details:
    - METHOD: PATCH
    - URL: `http://localhost:3000/quotes/{id}` (replace `{id}` with the quote ID you want to update)
    - Headers:
        - Content-Type: application/json
    - Request:

```shell
curl --request PATCH "http://localhost:3000/quotes/{id}" \
  --header "Content-Type: application/json" \
  --data '{
    "customQuote": true,
    "customQuoteText": "Your custom quote goes here."
  }'
```

Send the request.

A successful request returns a `200 OK` status code with the updated quote object in the response body.

## Example

Request:

```shell
curl --request PATCH "http://localhost:3000/quotes/3" \
  --header "Content-Type: application/json" \
  --data '{
    "customQuote": true,
    "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi"
  }'
```

Response body:

```json
{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
  "customQuote": true,
  "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi",
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct quote ID.
- `400 Bad Request`: Make sure your JSON is correctly formatted and includes both `customQuote` and `customQuoteText` fields.

## What's next?

Now that you've learned how to add a custom quote for a subscriber, you can:

- Implement a feature in your application for users to submit their own quotes.
- Create a moderation system for reviewing and approving custom quotes before they're added to the rotation.
- Develop a feature to display a subscriber's custom quote alongside quotes from the standard categories.
- Consider adding functionality to edit or delete custom quotes.
