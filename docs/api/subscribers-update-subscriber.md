---
layout: page
---

# Update a subscriber

This endpoint allows you to update a subscriber's information in the Quotable API, providing flexibility to modify subscriber details as needed.

You need to provide the subscriber's ID in the URL path and the updated subscriber details in the request body. The API will update the subscriber's information and return the updated subscriber object in the response.

## URL

```shell
{DELETE}{base_url}/subscribers/{id}
```

## Sample request

To remove a subscriber with ID 5, you would send the following request:

```shell
DELETE {base_url}/subscribers/5
```

## Sample response

Upon successful deletion of the subscriber, the API will return a `204 No Content` status code with an empty response body.

```text
HTTP/1.1 204 No Content
```

Note that when you delete a subscruber, all associated quotes for that subscriber are also deleted. This ensures data consistency and prevents orphaned quotes from remaining in the system.

If you attempt to remove a subscriber that does not exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The unique identifier of the subscriber to be updated. |

## Request headers

```shell
Content-Type: application/json
```

## Request body

This is the structure and fields of the JSON object that should be sent in the request body when updating a subscriber.

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

This is an example of a JSON object that can be sent in the request body when updating a subscriber.

```js
{
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "peter.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": true,
  "helpPplQuote": false,
  "deliverTo": 2,
  "frequency": 1
}
```

## Response body

This is the structure and fields of the JSON object that will be returned in the response body after successfully updating a subscriber.

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

After updating a subscriber, the API will return the updated subscriber object in the response body.

```js
{
  "id": 5,
  "lastName": "Parker",
  "firstName": "Peter",
  "email": "peter.parker@example.com",
  "mobile": "5551234567",
  "healthQuote": true,
  "loveQuote": true,
  "helpPplQuote": false,
  "deliverTo": 2,
  "frequency": 1
}
```

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 200 | OK | Subscriber successfully updated. |
| 400 | Bad Request | Invalid or missing parameters in the request body. |
| 404 | Not Found | Subscriber with the specified ID not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
