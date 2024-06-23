---
layout: default
title: Your Page Title
---

# Delete a quote

This endpoint allows you to remove a specific quote from the Quotable API when it is no longer needed or when it needs to be deleted from the system.

You need to provide the quote's ID in the URL path. The API will delete the quote and return a success status code if the deletion is successful.

## URL

```shell
{DELETE}{base_url}/quotes/{id}
```

## Sample request

To remove a quote with ID 3, you would send the following request:

```shell
DELETE {base_url}/quotes/3
```

## Sample response

Upon successful deletion of the quote, the API will return a `204 No Content` status code with an empty response body.

```text
HTTP/1.1 204 No Content
```

Note that when you delete a quote, it is permanently removed from the system. This action cannot be undone, so use this endpoint with caution.

If you attempt to remove a quote that doesn't exist, the API will return a `404 Not Found` status code.

## Params

| Parameter | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The unique identifier of the quote to be removed. |

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
| 204 | No Content | Quote successfully removed. |
| 404 | Not Found | Quote with the specified ID not found. |
| 500 | Internal server Error | An unexpected error occurred on the server. |
