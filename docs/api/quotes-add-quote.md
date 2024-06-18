---
layout: page
---

# Add a new quote for a subscriber

This endpoint allows you to add a new quote for a specific subscriber. You can provide the subscriber's ID along with the quote details. The API will create a new quote associated with the specified subscriber and return the created quote object in the response.

## URL

```shell
{POST}{base_url}/quotes/
```

## Params

None

## Request headers

```shell
Content-Type: application/json
```

## Request body

This is the structure and fields of the JSON object that should be sent in the request body when adding a new quote.

``` js
{
  "subscriberId": integer,
  "healthQuoteText": string,
  "loveQuoteText": string,
  "helpPplQuoteText": string,
  "customQuote": boolean,
  "customQuoteText": string,
  "shareQuote": boolean,
  "shareQuoteContact": string
}
```

## Sample request body

This is an example of a JSON object that can be sent in the request body when adding a new quote.

``` js
{
  "subscriberId": 2,
  "healthQuoteText": "",
  "loveQuoteText": "Love is not about possession. Love is about appreciation. – Osho",
  "helpPplQuoteText": "",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "bucky.barnes@example.com"
}
```

### Response body

This is the structure and fields of the JSON object that will be returned in the response body after successfully adding a new quote. Additionally, you'll get the `201 Created` status code.

``` js
{
  "subscriberId": integer,
  "id": integer,
  "healthQuoteText": string,
  "loveQuoteText": string,
  "helpPplQuoteText": string,
  "customQuote": boolean,
  "customQuoteText": string,
  "shareQuote": boolean,
  "shareQuoteContact": string
}
```

## Sample response body

Once a new quote has been created, this is the example response body you get:

```js
{
  "subscriberId": 2,
  "id": 6,
  "healthQuoteText": "",
  "loveQuoteText": "Love is not about possession. Love is about appreciation. – Osho",
  "helpPplQuoteText": "",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "bucky.barnes@example.com"
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 201 | Created | Quote successfully added for the subscriber. |
| 400 | Bad Request | Invalid or missing parameters in the request body. |
| 404 | Not Found | Subscriber with the specified subscriberId not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
