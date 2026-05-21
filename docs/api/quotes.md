---
layout: default
title: Quotes resource
---

# `quotes` resource

Use the `quotes` resource to manage quote records associated with subscribers.

## Base endpoint

```text
{base_url}/quotes
```

## Resource properties

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

| Property | Type | Required | Description |
| -------- | ---- | -------- | ----------- |
| `subscriberId` | integer | Required | ID of the subscriber associated with the quote. |
| `id` | integer | Required | Unique quote ID. JSON Server creates this value for new quotes. |
| `healthQuoteText` | string | Optional | Quote text from the Health category. |
| `loveQuoteText` | string | Optional | Quote text from the Love category. |
| `helpPplQuoteText` | string | Optional | Quote text from the Helping People category. |
| `customQuote` | boolean | Required | Whether the record contains a custom quote from the subscriber. |
| `customQuoteText` | string | Optional | Custom quote text. |
| `shareQuote` | boolean | Required | Whether to share the quote with another contact. |
| `shareQuoteContact` | string | Optional | Email address or phone number for sharing the quote. |

## Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/quotes` | [Retrieve all quotes](quotes-get-all-quotes.md). |
| <span class="method method--get">GET</span> | `/quotes/{id}` | [Retrieve one quote by ID](quotes-get-quote-by-id.md). |
| <span class="method method--post">POST</span> | `/quotes` | [Create a quote](quotes-add-quote.md). |
| <span class="method method--put">PUT</span> | `/quotes/{id}` | [Replace a quote](quotes-update-quote.md). |
| <span class="method method--delete">DELETE</span> | `/quotes/{id}` | [Delete a quote](quotes-delete-quote-by-id.md). |
