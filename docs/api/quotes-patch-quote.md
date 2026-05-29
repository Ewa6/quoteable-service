---
layout: default
title: Update a quote
---

# Update a quote

Updates one or more fields in an existing quote record.

## Method

<span class="method method--patch">PATCH</span>

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

Send only the quote fields that you want to update.

## Response body

Returns the updated quote.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | The quote was updated. |
| 400 | Bad Request | The request body is invalid JSON. |
| 404 | Not Found | No quote exists with the specified ID. |

## Example request

```shell
curl --request PATCH "http://localhost:3000/quotes/3" \
  --header "Content-Type: application/json" \
  --data '{
    "customQuote": true,
    "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi"
  }'
```

## Example response

```json
{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. - Denzel Washington",
  "customQuote": true,
  "customQuoteText": "Be the change you wish to see in the world. - Mahatma Gandhi",
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```
