---
layout: default
title: Change a subscriber's quote delivery method
---

# Change a subscriber's quote delivery method

This tutorial demonstrates how to update a subscriber's quote delivery method using the Quoteable Service API. This process lets subscribers choose whether they want to receive quotes by email or text message.

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
- A `deliverTo` value of `1` represents email delivery, and `2` represents text message delivery.
- In this mock API, JSON Server stores the delivery method value that you send. Add contact validation in your own application if you need it.
- Changing the delivery method doesn't affect the subscriber's quote preferences or frequency.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have a tool such as Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose delivery method you want to change.</li>
</ul>

## Change subscriber's quote delivery method

To change a subscriber's quote delivery method, send a `PATCH` request to the `/subscribers/{id}` endpoint with the updated `deliverTo` value.

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
    "deliverTo": 2
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
    "deliverTo": 2
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
  "deliverTo": 2,
  "frequency": 3
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber ID.
- `400 Bad Request`: Make sure your JSON is correctly formatted and the `deliverTo` value is either `1` or `2`.

## What's next?

Now that you've learned how to change a subscriber's quote delivery method, you can:

- Update other subscriber details, such as quote preferences or delivery frequency.
- Retrieve the updated subscriber information to confirm changes.
- Implement a feature in your application allowing users to toggle between email and text message delivery.
- Consider adding validation in your application to make sure the appropriate contact information (email or mobile) is available before changing the delivery method.
