---
layout: default
title: Update a subscriber's quote preferences
---

# Update a subscriber's quote preferences

This tutorial demonstrates how to update a subscriber's quote preferences using the Quoteable Service API. This process lets subscribers change which types of quotes they want to receive.

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

- You can update any combination of quote preferences (health, love, helping others) in a single request.
- If you only want to update one preference, only include that field in your request body.
- The API returns the entire updated subscriber object, including fields you didn't modify.
- In this mock API, JSON Server stores the preference values that you send. Add preference validation in your own application if you need it.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have a tool such as Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose preferences you want to update.</li>
</ul>

## Update subscriber's quote preferences

To update a subscriber's quote preferences, send a `PATCH` request to the `/subscribers/{id}` endpoint with the updated preference information.

For endpoint details, see [Update a subscriber](../api/subscribers-patch-subscriber.html).

Follow these steps:

1. Open your API testing tool, such as Postman.
2. Create a new request with the following details:
    - METHOD: PATCH
    - URL: `http://localhost:3000/subscribers/{id}` (replace `{id}` with the actual subscriber ID)
    - Headers:
        - Content-Type: application/json
    - Request:

```shell
curl --request PATCH "http://localhost:3000/subscribers/{id}" \
  --header "Content-Type: application/json" \
  --data '{
    "healthQuote": true,
    "loveQuote": false,
    "helpPplQuote": true
  }'
```

Send the request.

A successful request returns a `200 OK` status code with the updated subscriber object in the response body.

## Example

Request:

```shell
curl --request PATCH "http://localhost:3000/subscribers/1" \
  --header "Content-Type: application/json" \
  --data '{
    "healthQuote": true,
    "loveQuote": false,
    "helpPplQuote": true
  }'
```

Response body:

```json
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "tony.stark@example.com",
  "mobile": "2125551212",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber ID.
- `400 Bad Request`: Make sure your JSON is correctly formatted and contains valid boolean values.

## What's next?

Now that you've learned how to update a subscriber's quote preferences, you can:

- Update other subscriber details, such as delivery method or frequency.
- Retrieve the updated subscriber information to confirm changes.
- Use this method to build a preference management feature in your application.
