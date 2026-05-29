---
layout: default
title: Retrieve all quotes for a subscriber
---

# Retrieve all quotes for a subscriber

This tutorial demonstrates how to retrieve a subscriber with their quotes in a single API request by using the `_embed` parameter. By embedding the quotes, you can retrieve the subscriber information and associated quotes without making separate requests for each resource.

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
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have a tool such as Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Have the subscriber ID for the quotes that you want to retrieve.</li>
</ul>

## Retrieve subscriber with associated quotes

To retrieve a subscriber with their associated quotes, send a `GET` request to the `/subscribers/{id}` endpoint with the `_embed` parameter set to `quotes`.

To do so, follow these steps:

1. Open your API testing tool, such as Postman.
2. Create a new request with the following details:
    - METHOD: GET
    - URL: `http://localhost:3000/subscribers/{id}?_embed=quotes` (replace `{id}` with the actual subscriber ID)

Send the request.

A successful request returns the `200 OK` status code.

In the response, you see the subscriber object with an additional quotes array that contains all the associated quotes for that subscriber.

## Example

Request:

```shell
curl "http://localhost:3000/subscribers/1?_embed=quotes"
```

Response body:

```json
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
      "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
      "loveQuoteText": "",
      "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
      "customQuote": false,
      "customQuoteText": "",
      "shareQuote": true,
      "shareQuoteContact": "pepper.pots@stark.com"
    }
  ]
}
```

## What's next?

After completing this tutorial, you can explore other endpoints and parameters provided by the Quoteable Service API to retrieve and manipulate data according to your application's requirements.
