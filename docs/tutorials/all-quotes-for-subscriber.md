---
layout: page
---

# Retrieve all quotes for a subscriber

This tutorial demonstrates how to retrieve a subscriber along with their quotes in a single API request using the `_embed` parameter. By embedding the quotes, you can efficiently retrieve the subscriber's information and their associated quotes without making separate requests for each resource.

> :clock1: **Expected duration:** Expect this tutorial to take about 10 minutes to complete.

## Prerequisites

Before you start this tutorial:

- [x] Ensure you have access to the Quotable API.
- [ ] Ensure you have a tool like Postman or cURL installed to make API requests.
- [ ] Have the `subscriberId` for which you want to retrieve the quotes.

## Retrieve subscriber with associated quotes

To retrieve a subscriber along with their associated quotes, you need to send a `GET` request to the `/subscribers/{id}` endpoint with the `_embed` parameter set to quotes.

To do so, follow these steps:

1. Open your API testing tool (e.g., Postman).
2. Create a new request with the following details:
    - METHOD: GET
    - URL: `{{base_url}}/subscribers/{id}?_embed=quotes` (replace `{id}` with the actual subscriberId)
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
      "quoteDate": "2018-03-20T22:00",
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

After completing this tutorial, you can explore other endpoints and parameters provided by the Quotable API to retrieve and manipulate data according to your application's requirements.
