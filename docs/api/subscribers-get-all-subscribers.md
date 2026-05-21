---
layout: default
title: Retrieve all subscribers
---

# Retrieve all subscribers

Returns all subscriber records.

## Method

<span class="method method--get">GET</span>

## Endpoint

```text
{base_url}/subscribers
```

## Path parameters

None.

## Query parameters

None.

## Headers

None.

## Request body

None.

## Response body

```json
[
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
]
```

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The request succeeded. |

## Example request

```shell
curl "http://localhost:3000/subscribers"
```

## Example response

```json
[
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
  },
  {
    "id": 2,
    "lastName": "Rogers",
    "firstName": "Stephen",
    "email": "s.rogers@example.com",
    "mobile": "7185551212",
    "healthQuote": false,
    "loveQuote": true,
    "helpPplQuote": true,
    "deliverTo": 2,
    "frequency": 1
  }
]
```
