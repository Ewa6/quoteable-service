---
layout: page
---

# Get a subscriber by ID

This endpoint allows you to retrieve a specific subscriber by their ID from the Quotable API.

You need to provide the `subscriberId` in the URL path, and the API will return the corresponding quote object if it exist

## URL

```shell
{GET}{base_url}/subscribers/{id}
```

## Sample request

To retrieve a subscriber with ID 3, you would send the following request:

```shell
GET {base_url}/subscribers/3
```

## Sample response

Upon successful retrieval of the subscriber, the API will return a `200 OK` status code with the subscriber object in the response body.

```js
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "t.stark@example.com",
  "mobile": "2125551212",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3
}
```

If the subscriber with the specified ID does not exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The unique identifier of the subscriber to be retrieved. |

## Request headers

```shell
Content-Type: application/json
```

## Request body

None

## Response body

This is the structure and fields of the JSON object that will be returned in the response body if the subscriber with the specified ID exists.

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

If the subscriber with the specified ID exists, this is the example response body you get:

```js
{
  "id": 1,
  "lastName": "Stark",
  "firstName": "Tony",
  "email": "t.stark@example.com",
  "mobile": "2125551212",
  "healthQuote": true,
  "loveQuote": false,
  "helpPplQuote": true,
  "deliverTo": 1,
  "frequency": 3
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 200 | OK | Subscriber successfully retrieved. |
| 404 | Not Found | Subscriber with the specified ID not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
