---
layout: default
title: Retrieve all quotes
---

# Retrieve all quotes

Returns all quote records.

## Method

<span class="method method--get">GET</span>

## Endpoint

```text
{base_url}/quotes
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
    "subscriberId": 1,
    "id": 3,
    "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
    "loveQuoteText": "",
    "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": true,
    "shareQuoteContact": "pepper.pots@stark.com"
  }
]
```

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The request succeeded. |

## Example request

```shell
curl "http://localhost:3000/quotes"
```

## Example response

```json
[
  {
    "subscriberId": 1,
    "id": 3,
    "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
    "loveQuoteText": "",
    "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": true,
    "shareQuoteContact": "pepper.pots@stark.com"
  },
  {
    "subscriberId": 2,
    "id": 1,
    "healthQuoteText": "",
    "loveQuoteText": "When we lose someone we love, we must learn not to live without them, but to live with the love they left behind. - Unknown",
    "helpPplQuoteText": "If you're not making someone else's life better, then you're wasting your time. - Will Smith",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": false,
    "shareQuoteContact": ""
  }
]
```
