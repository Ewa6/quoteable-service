---
layout: default
title: Retrieve a subscriber by ID
---

# Retrieve a subscriber by ID

Returns one subscriber by ID.

## Method

<span class="method method--get">GET</span>

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

None.

## Request body

None.

## Response body

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

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The subscriber was found. |
| 404 | Not Found | No subscriber exists with the specified ID. |

## Example request

```shell
curl "http://localhost:3000/subscribers/1"
```

## Example response

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
