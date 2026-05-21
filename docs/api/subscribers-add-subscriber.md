---
layout: default
title: Create a subscriber
---

# Create a subscriber

Creates a subscriber record. JSON Server assigns the `id`.

## Method

<span class="method method--post">POST</span>

## Endpoint

```text
{base_url}/subscribers
```

## Path parameters

None.

## Query parameters

None.

## Headers

| Header | Required | Value |
| ------ | -------- | ----- |
| `Content-Type` | Required | `application/json` |

## Request body

| Property | Type | Required | Description |
| -------- | ---- | -------- | ----------- |
| `lastName` | string | Required | Subscriber's last name. |
| `firstName` | string | Required | Subscriber's first name. |
| `email` | string | Required | Subscriber's email address. |
| `mobile` | string | Optional | Subscriber's mobile phone number. |
| `healthQuote` | boolean | Optional | Whether the subscriber wants Health quotes. |
| `loveQuote` | boolean | Required | Whether the subscriber wants Love quotes. |
| `helpPplQuote` | boolean | Optional | Whether the subscriber wants Helping People quotes. |
| `deliverTo` | integer | Required | Delivery method. Use `1` for email and `2` for text message. |
| `frequency` | integer | Required | Delivery frequency. Use `1` for daily, `2` for weekly, and `3` for monthly. |

## Response body

Returns the created subscriber, including the generated `id`.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 201 | Created | The subscriber was created. |
| 400 | Bad Request | The request body is invalid. |

## Example request

```shell
curl --request POST "http://localhost:3000/subscribers" \
  --header "Content-Type: application/json" \
  --data '{
    "lastName": "Parker",
    "firstName": "Peter",
    "email": "p.parker@example.com",
    "mobile": "5551234567",
    "healthQuote": true,
    "loveQuote": false,
    "helpPplQuote": true,
    "deliverTo": 1,
    "frequency": 2
  }'
```

## Example response

```json
{
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "p.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2,
  "id": 5
}
```
