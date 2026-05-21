---
layout: default
title: Subscribers resource
---

# `subscribers` resource

Use the `subscribers` resource to manage people who receive quotes from the Quoteable Service.

## Base endpoint

```text
{base_url}/subscribers
```

## Resource properties

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
  "frequency": 3
}
```

| Property | Type | Required | Description |
| -------- | ---- | -------- | ----------- |
| `id` | integer | Required | Unique subscriber ID. JSON Server creates this value for new subscribers. |
| `lastName` | string | Required | Subscriber's last name. |
| `firstName` | string | Required | Subscriber's first name. |
| `email` | string | Required | Subscriber's email address. |
| `mobile` | string | Optional | Subscriber's mobile phone number. |
| `healthQuote` | boolean | Optional | Whether the subscriber wants quotes from the Health category. |
| `loveQuote` | boolean | Required | Whether the subscriber wants quotes from the Love category. |
| `helpPplQuote` | boolean | Optional | Whether the subscriber wants quotes from the Helping People category. |
| `deliverTo` | integer | Required | Delivery method. Use `1` for email and `2` for text message. |
| `frequency` | integer | Required | Delivery frequency. Use `1` for daily, `2` for weekly, and `3` for monthly. |

## Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/subscribers` | [Retrieve all subscribers](subscribers-get-all-subscribers.html). |
| <span class="method method--get">GET</span> | `/subscribers/{id}` | [Retrieve one subscriber by ID](subscribers-get-subscriber-by-id.html). |
| <span class="method method--post">POST</span> | `/subscribers` | [Create a subscriber](subscribers-add-subscriber.html). |
| <span class="method method--put">PUT</span> | `/subscribers/{id}` | [Replace a subscriber](subscribers-update-subscriber.html). |
| <span class="method method--delete">DELETE</span> | `/subscribers/{id}` | [Delete a subscriber](subscribers-delete-subscriber.html). |
