---
layout: page
---

# Add a new subscriber

This endpoint allows you to create a new subscriber in the Quotable API. You can provide the subscriber's details, including their name, email, mobile number, quote preferences, delivery method, and frequency. The API will create a new subscriber and return the created subscriber object in the response.

## URL

```shell
{POST}{base_url}/subscribers/
```

## Sample request

To create a new subscriber, send the following request:

```shell
POST {base_url}/subscribers/
Content-Type: application/json

{
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "p.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2
}
```

## Sample response

Upon successful creation of the subscriber, the API will return a `201 Created` status code with the created subscriber object in the response body.

```js
{
  "id": 5,
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "p.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2
}
```

## Params

None

## Request headers

```shell
Content-Type: application/json
```

## Request body

This is the structure and fields of the JSON object that should be sent in the request body when adding a new subscriber.

```js
{
  "lastName": string,
  "firstName": string,
  "email": string,
  "mobile": string,
  "healthQuote": boolean,
  "loveQuote": boolean,
  "helpPplQuote": boolean,
  "deliverTo": integer,
  "frequency": integer
}
```

## Sample request body

This is an example of a JSON object that can be sent in the request body when adding a new subscriber.

```js
{
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "p.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2
}
```

## Response body

This is the structure and fields of the JSON object that will be returned in the response body after successfully adding a new subscriber.

```js
{
  "id": integer,
  "lastName": string,
  "firstName": string,
  "email": string,
  "mobile": string,
  "healthQuote": boolean,
  "loveQuote": boolean,
  "helpPplQuote": boolean,
  "deliverTo": integer,
  "frequency": integer
}
```

## Sample response body

Once a new subscriber has been created, this is the example response body you get:

```js
{
  "id": 5,
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "p.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 2
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 201 | Created | Subscriber successfully created. |
| 400 | Bad Request | Invalid or missing parameters in the request body. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
