---
layout: default
title: Your Page Title
---

# Update a quote

This endpoint allows you to update an existing quote in the Quoteable API.

You can modify the quote's text, custom quote status, sharing preferences, and other properties. The API will update the quote and return the updated quote object in the response.

## URL

```shell
{PUT}{base_url}/quotes/{id}
```

## Sample request

To update an existing quote, send the following request:

```shell
PUT {base_url}/quotes/3
Content-Type: application/json

{
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
  "customQuote": false,
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```

## Sample response

Upon successful update of the quote, the API will return a `200 OK` status code with the updated quote object in the response body.

```js
HTTP/1.1 200 OK
Content-Type: application/json

{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```

If the quote with the specified ID does not exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The unique identifier of the quote to update |

## Request headers

```shell
Content-Type: application/json
```

## Request body

This is the structure and fields of the JSON object that should be sent in the request body when updating a quote.

```js
{
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

This is an example of a JSON object that can be sent in the request body when updating a quote.

```js
{
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
  "customQuote": false,
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```

## Response body

This is the structure and fields of the JSON object that will be returned in the response body after successfully updating a quote.

```js
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

Once a quote has been updated, this is the example response body you get:

```js
{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "The greatest wealth is health. - Virgil",
  "loveQuoteText": "",
  "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
  "customQuote": false,
  "customQuoteText": "",
  "shareQuote": true,
  "shareQuoteContact": "pepper.pots@stark.com"
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 200 | OK | Quote successfully updated. |
| 400 | Bad Request | Invalid or missing parameters in the request body. |
| 404 | Not Found | Quote with the specified ID doesn't exist |
| 500 | Internal server Error | An unexpected error occurred on the server. |
