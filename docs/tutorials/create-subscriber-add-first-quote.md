---
layout: default
title: Create a subscriber and add their first quote
---

# Create a subscriber and add their first quote

This tutorial demonstrates how to create a subscriber in the Quoteable Service API and then add their first quote. Follow these steps to use multiple endpoints to set up a new user in the system and provide them with their initial quote.

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
  <li style="list-style-type: none;"><input type="checkbox"> Familiarize yourself with the structure of <code>subscriber</code> and <code>quote</code> objects in the API.</li>
</ul>

## Step 1: Create a new subscriber

First, create a new subscriber by sending a `POST` request to the `/subscribers` endpoint.

1. Open your API testing tool, such as Postman.
2. Create a new request with the following details:
    - METHOD: POST
    - URL: `http://localhost:3000/subscribers`
    - Headers:
        - Content-Type: application/json
    - Request:

```shell
curl --request POST "http://localhost:3000/subscribers" \
  --header "Content-Type: application/json" \
  --data '{
    "lastName": "Doe",
    "firstName": "Jane",
    "email": "jane.doe@example.com",
    "mobile": "5551234567",
    "healthQuote": true,
    "loveQuote": true,
    "helpPplQuote": false,
    "deliverTo": 1,
    "frequency": 2
  }'
```

Send the request.

A successful request returns the `201 Created` status code with the newly created subscriber object in the response body. Note the `id` of the new subscriber because you need it for the next step.

## Step 2: Add the first quote for the new subscriber

Now that you have created a new subscriber, add their first quote by sending a `POST` request to the `/quotes` endpoint.

1. Create another new request in your API testing tool with these details:
    - METHOD: POST
    - URL: `http://localhost:3000/quotes`
    - Headers:
        - Content-Type: application/json
    - Request:

```shell
curl --request POST "http://localhost:3000/quotes" \
  --header "Content-Type: application/json" \
  --data '{
    "subscriberId": 5,
    "healthQuoteText": "The greatest wealth is health. - Virgil",
    "loveQuoteText": "Where there is love there is life. - Mahatma Gandhi",
    "helpPplQuoteText": "",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": true,
    "shareQuoteContact": "friend@example.com"
  }'
```

Replace `5` with the actual `id` of the subscriber you created in Step 1.

Send the request.

A successful request returns the `201 Created` status code with the newly created quote object in the response body.

## Example

Step 1: Response body (Create subscriber):

```json
{
  "id": 5,
  "lastName": "Doe",
  "firstName": "Jane",
  "email": "jane.doe@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": true,
  "helpPplQuote": false,
  "deliverTo": 1,
  "frequency": 2
}
```

Step 2: Response body (Add quote):

```json
{
  "subscriberId": 5,
  "id": 6,
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "Where there is love there is life. - Mahatma Gandhi",
  "helpPplQuoteText": "",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "friend@example.com"
}
```

## What's next?

After completing this tutorial, you have successfully created a subscriber and added their first quote. You can explore other endpoints and parameters provided by the Quoteable Service API to retrieve, update, or delete subscribers and quotes according to your application's requirements.

Some next steps you might consider:

- Retrieve all quotes for the newly created subscriber
- Update the subscriber's preferences
- Add more quotes for the subscriber
