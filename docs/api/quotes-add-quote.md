---
layout: default
title: Create a quote
---

# Create a quote

Creates a quote record and associates it with a subscriber.

## Method

<span class="method method--post">POST</span>

## Endpoint

```text
{base_url}/quotes
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
| `subscriberId` | integer | Required | ID of the subscriber associated with the quote. |
| `healthQuoteText` | string | Optional | Health quote text. |
| `loveQuoteText` | string | Optional | Love quote text. |
| `helpPplQuoteText` | string | Optional | Helping People quote text. |
| `customQuote` | boolean | Required | Whether this is a custom quote. |
| `customQuoteText` | string | Optional | Custom quote text. |
| `shareQuote` | boolean | Required | Whether to share the quote. |
| `shareQuoteContact` | string | Optional | Contact for sharing the quote. |

## Response body

Returns the created quote, including the generated `id`.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 201 | Created | The quote was created. |
| 400 | Bad Request | The request body is invalid. |

## Example request

```shell
curl --request POST "http://localhost:3000/quotes" \
  --header "Content-Type: application/json" \
  --data '{
    "subscriberId": 2,
    "healthQuoteText": "",
    "loveQuoteText": "Love is not about possession. Love is about appreciation. - Osho",
    "helpPplQuoteText": "",
    "customQuote": false,
    "customQuoteText": "",
    "shareQuote": true,
    "shareQuoteContact": "bucky.barnes@example.com"
  }'
```

## Example response

```json
{
  "subscriberId": 2,
  "healthQuoteText": "",
  "loveQuoteText": "Love is not about possession. Love is about appreciation. - Osho",
  "helpPplQuoteText": "",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "bucky.barnes@example.com",
  "id": 6
}
```
