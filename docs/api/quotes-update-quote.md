---
layout: default
title: Replace a quote
---

# Replace a quote

Replaces an existing quote record.

## Method

<span class="method method--put">PUT</span>

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

| Header | Required | Value |
| ------ | -------- | ----- |
| `Content-Type` | Required | `application/json` |

## Request body

Send the complete quote object without the `id`.

## Response body

Returns the updated quote.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The quote was updated. |
| 400 | Bad Request | The request body is invalid. |
| 404 | Not Found | No quote exists with the specified ID. |

## Example request

```shell
curl --request PUT "http://localhost:3000/quotes/3" \
  --header "Content-Type: application/json" \
  --data '{
    "subscriberId": 1,
    "healthQuoteText": "The greatest wealth is health. - Virgil",
    "loveQuoteText": "",
    "helpPplQuoteText": "Helping others creates lasting impact. - Quoteable Service",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": true,
    "shareQuoteContact": "pepper.pots@stark.com"
  }'
```

## Example response

```json
{
  "subscriberId": 1,
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com",
  "id": 3
}
```
