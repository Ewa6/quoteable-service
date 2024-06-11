---
layout: page
---

# `quotes` resource

With the `quotes` resource you can manage and retrieve quotes associated with subscribers in the Quoteable API. It allows you to:

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
        "quoteDate": "2018-03-20T22:00",
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
| `subscriberId` | number | The subscriber's unique ID. | :white_check_mark: |
| `id` | number | The unique ID of the quote. | :white_check_mark: |
| `quoteDate` | string | The date when the subsciber gets the quote(s). It's in the following date and time format: `YYYY-MM-DDTHH:mm` | :white_check_mark: |
| `healthQuoteText` | string | The text of the quote from the **Health** category.  | :x: |
| `loveQuoteText` | string | The text of the quote from the  **Love** category.| :x: |
| `helpPplQuoteText` | strong | The text of the quote from the **Helping People** category. | :x: |
| `customQuote` | Boolean | Indicates whether the subscriber wants to add a custom quote. | :white_check_mark:  |
| `customQuoteText` | string | A custom quote text. | :x: |
| `shareQuote` | Boolean | Indicates whether the subscriber wants to share the quote. | :white_check_mark: |
| `shareQuoteContact` | string | The email of a person to share the quote with. | :white_check_mark: |

## CRUD Operations

See API reference below to see which CRUD actions supports the `quotes` resource.

### Create (POST)

Add a new quote for a subscriber

### Read (GET)

Get all quotes
Get a quote by ID
Get quotes by date

### Update (PUT/PATCH)

Update a quote
Add a custom quote for a subscriber
Update a contact person for sharing a quote

### Delete (DELETE)

Delete a quote by ID
