---
layout: default
title: Update a subscriber
---

# Update a subscriber

Updates one or more fields in an existing subscriber record.

## Method

<span class="method method--patch">PATCH</span>

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

Send only the subscriber fields that you want to update.

## Response body

Returns the updated subscriber.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The subscriber was updated. |
| 400 | Bad Request | The request body is invalid JSON. |
| 404 | Not Found | No subscriber exists with the specified ID. |

## Example request

```shell
curl --request PATCH "http://localhost:3000/subscribers/1" \
  --header "Content-Type: application/json" \
  --data '{
    "email": "tony.stark.new@example.com",
    "frequency": 2
  }'
```

## Example response

```json
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "tony.stark.new@example.com",
  "mobile": "2125551212",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2
}
```
