---
layout: default
title: Your Page Title
---

# Delete a subscriber

This endpoint provides a simple way to remove subscribers from the Quoteable API when they are no longer needed or when they request to be deleted from the system.

You need to provide the subscriber's ID in the URL path. The API will delete the subscriber and return a success status code if the deletion is successful.

## URL

```shell
{DELETE}{base_url}/subscribers/{id}
```

## Sample request

To remove a subscriber with ID 5, send the following request:

```shell
DELETE {base_url}/subscribers/5
```

## Sample response

Upon successful deletion of the subscriber, the API will return a `204 No Content` status code with an empty response body.

```text
HTTP/1.1 204 No Content
```

Note that when you delete a subscriber, all associated quotes for that subscriber are also deleted. This ensures data consistency and prevents orphaned quotes from remaining in the system.

If you attempt to remove a subscriber that does not exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The unique identifier of the subscriber to be removed. |

## Request headers

```shell
Content-Type: application/json
```

## Request body

None

## Response body

None

## Return status

The table below lists the possible HTTP status codes that can be returned by the API, along with their corresponding meanings.

| HTTP Status Code | Return status | Description |
| ------------- | ----------- | ----------- |
| 204 | No Content | Subscriber successfully removed. |
| 404 | Not Found | Subscriber with the specified ID not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
