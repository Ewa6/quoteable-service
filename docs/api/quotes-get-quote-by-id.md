---
layout: default
title: Retrieve a quote by ID
---

# Retrieve a quote by ID

Returns one quote by ID.

## Method

<span class="method method--get">GET</span>

## Endpoint

```text
{base_url}/quotes/{id}
```

## Path parameters

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer | Required | Unique quote ID. |

## Query parameters

None.

## Headers

None.

## Request body

None.

## Response body

```json
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
```

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The quote was found. |
| 404 | Not Found | No quote exists with the specified ID. |

## Example request

```shell
curl "http://localhost:3000/quotes/3"
```

## Example response

```json
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
```
