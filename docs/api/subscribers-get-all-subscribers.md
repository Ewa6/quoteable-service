---
layout: default
title: Your Page Title
---

# Get all subscribers

Returns an array of `subscribers` objects that contains all subscribers that have registered to receive the quotes.

## Method

GET

## URL

```shell
{server_url}/subscribers
```

## Params

None

## Request headers

```shell
Content-Type: application/json
```

## Request body

None

## Return body

```js
[
    {
        "id": 1,
        "lastName": "Stark",
        "firstName": "Tony",
        "email": "t.stark@example.com",
        "mobile": "2125551212",
        "healthQuote": "True",
        "loveQuote": "False",
        "helpPplQuote": "True",
        "deliverTo": 1,
        "frequency": 3
    },
    {
        "id": 2,
        "lastName": "Rogers",
        "firstName": "Stephen",
        "email": "s.rogers@example.com",
        "mobile": "7185551212",
        "healthQuote": "False",
        "loveQuote": "True",
        "helpPplQuote": "True",
        "deliverTo": 2,
        "frequency": 1
    },
    {
        "id": 3,
        "lastName": "Odinson",
        "firstName": "Thor",
        "email": "t.odinson@example.com",
        "mobile": "",
        "healthQuote": "False",
        "loveQuote": "True",
        "helpPplQuote": "False",
        "deliverTo": 2,
        "frequency": 2
    },
    {
        "id": 4,
        "lastName": "Romanov",
        "firstName": "Natasha",
        "email": "n.romanov@example.com",
        "mobile": "2025551212",
        "healthQuote": "True",
        "loveQuote": "True",
        "helpPplQuote": "True",
        "deliverTo": 1,
        "frequency": 1
    }
]
```

## Return status

| Status value | Return status | Description |
| ------------- | ----------- | ----------- |
| 200 | Success | Requested data returned successfully |
| ECONNREFUSED | N/A | Service is offline. Start the service and try again. |
