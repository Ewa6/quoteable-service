---
layout: default
title: Your Page Title
---

# Retrieve all quotes for a subscriber

This tutorial demonstrates how to retrieve a subscriber along with their quotes in a single API request using the `_embed` parameter. By embedding the quotes, you can efficiently retrieve the subscriber's information and their associated quotes without making separate requests for each resource.

<div class="tutorial-duration">
  <div class="icon-container">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="12 6 12 12 16 14"></polyline>
    </svg>
  </div>
  <div class="duration-text"><strong>Expected duration:</strong> Expect this tutorial to take about 15 minutes to complete.</div>
</div>

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have access to the Quoteable API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Ensure you have a tool like Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Have the <code>subscriberId</code> for which you want to retrieve the quotes.</li>
</ul>

## Retrieve subscriber with associated quotes

To retrieve a subscriber along with their associated quotes, you need to send a `GET` request to the `/subscribers/{id}` endpoint with the `_embed` parameter set to quotes.

To do so, follow these steps:

1. Open your API testing tool (e.g., Postman).
2. Create a new request with the following details:
    - METHOD: GET
    - URL: `{{base_url}}/subscribers/{id}?_embed=quotes` (replace `{id}` with the actual `subscriberId`)
    - Headers:
        - Content-Type: application/json
        - Add any required authentication headers (if applicable).
3. Send the request.

The successful request should return the status code `200 OK`.

In the response, you will see the subscriber object with an additional quotes array containing all the associated quotes for that subscriber.

## Example

Request:

```js
GET {{base_url}}/subscribers/1?_embed=quotes
```

Response body:

```js
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "t.stark@example.com",
  "mobile": "2125551212",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3,
  "quotes": [
    {
      "subscriberId": 1,
      "id": 3,
      "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. – Anne Wilson Schaef",
      "loveQuoteText": "",
      "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
      "customQuote": false,
      "customQuoteText": "",
      "shareQuote": true,
      "shareQuoteContact": "pepper.pots@stark.com"
    }
  ]
}
```

## What's next?

After completing this tutorial, you can explore other endpoints and parameters provided by the Quoteable API to retrieve and manipulate data according to your application's requirements.
