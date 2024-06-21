---
layout: page
---

# Add a custom quote for a subscriber

This endpoint allows you to add a custom quote for a specific subscriber in the Quotable API.

You can provide the subscriber's ID and the custom quote text. The API will create a new quote entry with the custom quote and return the created quote object in the response.

## URL

```shell
{POST}{base_url}/quotes/custom/{subscriberId}
```

## Sample request

To add a custom quote for a subscriber, send the following request:

```shell
PUT {base_url}/quotes/3
Content-Type: application/json

{
  "customQuoteText": "With great power comes great responsibility. - Uncle Ben",
  "shareQuote": true,
  "shareQuoteContact": "may.parker@example.com"
}
```

## Sample response

Upon successful addition of the custom quote, the API will return a `201 Created` status code with the updated quote object in the response body.

```js
HTTP/1.1 200 OK
Content-Type: application/json

{
  "subscriberId": 1,
  "id": 6,
  "healthQuoteText": "",
  "loveQuoteText": "",
  "helpPplQuoteText": "",
  "customQuote": true,
  "customQuoteText": "With great power comes great responsibility. - Uncle Ben",
  "shareQuote": true,
  "shareQuoteContact": "may.parker@example.com"
}
```

If the quote subscriber the specified ID does not exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `subscriberId` | integer | The unique identifier of the subscriber for whom to add the custom quote. |

## Request headers

```shell
Content-Type: application/json
```

## Request body

This is the structure and fields of the JSON object that should be sent in the request body when adding a custom quote.

```js
{
  "customQuoteText": string,
  "shareQuote": boolean,
  "shareQuoteContact": string
}
```

## Sample request body

This is an example of a JSON object that can be sent in the request body when adding a custom quote.

```js
{
  "customQuoteText": "With great power comes great responsibility. - Uncle Ben",
  "shareQuote": true,
  "shareQuoteContact": "may.parker@example.com"
}
```

## Response body

This is the structure and fields of the JSON object that will be returned in the response body after successfully adding a custom quote.

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

Once a custom quote has been added, this is the example response body you get:

```js
{
  "subscriberId": 1,
  "id": 6,
  "healthQuoteText": "",
  "loveQuoteText": "",
  "helpPplQuoteText": "",
  "customQuote": true,
  "customQuoteText": "With great power comes great responsibility. - Uncle Ben",
  "shareQuote": true,
  "shareQuoteContact": "may.parker@example.com"
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 201 | Created | QCustom quote successfully added. |
| 400 | Bad Request | Invalid or missing parameters in the request body. |
| 404 | Not Found | Subscriber with the specified ID does not exist. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
