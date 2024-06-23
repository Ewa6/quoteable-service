---
layout: default
title: Your Page Title
---

# `quotes` resource

With the `quotes` resource you can manage and retrieve quotes associated with subscribers in the Quoteable Service. It allows you to:

* Retrieve quotes.
* Add new quotes.
* Update existing quotes.
* Remove quotes

## Base endpoint

```shell
{server_url}/quotes
```

## Resource properties

Sample `quotes` resource

```js
{
        "subscriberId": 1,
        "id": 3,
        "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. – Anne Wilson Schaef",
        "loveQuoteText": "",
        "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It’s about what you've given back. – Denzel Washington",
        "customQuote": "False",
        "customQuoteText": "",
        "shareQuote": "True",
        "shareQuoteContact": "pepper.pots@stark.com"
    }
```

| Property name | Type | Description | Mandatory |
| ------------- | ----------- | ----------- |     :----:    |
| `subscriberId` | number | The subscriber's unique ID. | ✅ |
| `id` | number | The unique ID of the quote. | ✅ |
| `healthQuoteText` | string | The text of the quote from the **Health** category.  | ❌ |
| `loveQuoteText` | string | The text of the quote from the  **Love** category. It's the default category. | ✅ |
| `helpPplQuoteText` | string | The text of the quote from the **Helping People** category. | ❌ |
| `customQuote` | Boolean | Indicates whether the subscriber wants to add a custom quote. | ✅  |
| `customQuoteText` | string | A custom quote text. | ❌ |
| `shareQuote` | Boolean | Indicates whether the subscriber wants to share the quote. | ✅ |
| `shareQuoteContact` | string | The email of a person to share the quote with. | ✅ |

## CRUD Operations

See API reference below to see which CRUD actions supports the `quotes` resource.

### Read (GET)

[Get all quotes](quotes-get-all-quotes.md)

[Get a quote by ID](quotes-get-quote-by-id.md)

### Create (POST)

[Add a new quote for a subscriber](quotes-add-quote.md)

### Update (PUT/PATCH)

[Update a quote](quotes-update-quote.md)

### Delete (DELETE)

[Delete a quote by ID](quotes-delete-quote-by-id.md)
