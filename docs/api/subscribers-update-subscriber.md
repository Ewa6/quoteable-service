---
layout: default
title: Replace a subscriber
---

# Replace a subscriber

Replaces an existing subscriber record.

## Method

<span class="method method--put">PUT</span>

## Endpoint

```text
{base_url}/subscribers/{id}
```

## Path parameters

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer | Required | Unique subscriber ID. |

## Query parameters

None.

## Headers

| Header | Required | Value |
| ------ | -------- | ----- |
| `Content-Type` | Required | `application/json` |

## Request body

Send the complete subscriber object without the `id`.

## Response body

Returns the updated subscriber.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The subscriber was updated. |
| 400 | Bad Request | The request body is invalid. |
| 404 | Not Found | No subscriber exists with the specified ID. |

## Example request

```shell
curl --request PUT "http://localhost:3000/subscribers/5" \
  --header "Content-Type: application/json" \
  --data '{
    "lastName": "Parker",
    "firstName": "Peter",
    "email": "peter.parker@example.com",
    "mobile": "5551234567",
    "healthQuote": true,
    "loveQuote": true,
    "helpPplQuote": false,
    "deliverTo": 2,
    "frequency": 1
  }'
```

## Example response

```json
{
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "peter.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": true,
  "helpPplQuote": false,
  "deliverTo": 2,
  "frequency": 1,
  "id": 5
}
```
