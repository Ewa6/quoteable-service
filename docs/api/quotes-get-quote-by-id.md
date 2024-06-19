---
layout: page
---

# Get a quote by ID

This endpoint allows you to retrieve a specific quote by its ID from the Quotable API. 

You need to provide the `quoteId` in the URL path, and the API will return the corresponding quote object if it exist

## URL

```shell
{GET}{base_url}/quotes/{id}
```

## Sample request

To retrieve a quote with ID 3, you would send the following request:

```shell
GET {base_url}/quotes/3
```

## Sample response

Upon successful retrieval of the quote, the API will return a `200 OK` status code with the quote object in the response body.

```js
{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. – Anne Wilson Schaef",
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
| `id` | integer | The unique identifier of the quote to be retrieved. |

## Request headers

```shell
Content-Type: application/json
```

## Request body

None

## Response body

This is the structure and fields of the JSON object that will be returned in the response body if the quote with the specified ID exists.

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

If the quote with the specified ID exists, this is the example response body you get:

```js
{
  "subscriberId": 1,
  "id": 3,
  "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. – Anne Wilson Schaef",
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
| 200 | OK | Quote successfully retrieved. |
| 404 | Not Found | Quote with the specified ID not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
