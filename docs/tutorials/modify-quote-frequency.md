---
layout: default
title: Modify a subscriber's quote frequency
---

# Modify a subscriber's quote frequency

This tutorial demonstrates how to update a subscriber's quote frequency using the Quoteable Service API. This process lets subscribers choose how often they want to receive quotes.

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
- A `frequency` value of `1` represents daily delivery, `2` represents weekly delivery, and `3` represents monthly delivery.
- Changing the frequency doesn't affect the subscriber's quote preferences or delivery method.
- In this mock API, JSON Server stores the frequency value that you send. Add range validation in your own application if you need it.

## Prerequisites

Before you start this tutorial:

<ul class="checkbox-list" style="list-style-type: none;">
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have access to the Quoteable Service API.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Make sure you have a tool such as Postman or cURL installed to make API requests.</li>
  <li style="list-style-type: none;"><input type="checkbox"> Know the <code>id</code> of the subscriber whose quote frequency you want to modify.</li>
</ul>

## Modify subscriber's quote frequency

To modify a subscriber's quote frequency, send a `PATCH` request to the `/subscribers/{id}` endpoint with the updated `frequency` value.

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
    "frequency": 2
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
    "frequency": 2
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
  "frequency": 2
}
```

## Error handling

If you encounter errors, here are some common issues and their solutions:

- `404 Not Found`: Check that you're using the correct subscriber ID.
- `400 Bad Request`: Make sure your JSON is correctly formatted and the frequency value is `1`, `2`, or `3`.

## What's next?

Now that you've learned how to modify a subscriber's quote frequency, you can:

- Update other subscriber details, such as quote preferences or delivery method.
- Retrieve the updated subscriber information to confirm changes.
- Implement a feature in your application allowing users to choose their preferred quote frequency.
- Consider adding a feature to your application that suggests changing the frequency based on user engagement. For example, it can suggest less frequent quotes if the user isn't opening daily emails.
