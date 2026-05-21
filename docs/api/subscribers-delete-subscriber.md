---
layout: default
title: Delete a subscriber
---

# Delete a subscriber

Deletes a subscriber record.

<div class="warning">
Deleting a subscriber does not automatically delete related quote records in JSON Server. Delete related quotes separately if you need to remove them.
</div>

## Method

<span class="method method--delete">DELETE</span>

## Endpoint

```text
{base_url}/subscribers/{id}
```

## Path parameters

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer | Required | Unique subscriber ID. |

## Query parameters

None.

## Headers

None.

## Request body

None.

## Response body

None.

## Status codes

| Status code | Status | Description |
| ----------- | ------ | ----------- |
| 200 | OK | JSON Server deleted the subscriber and returned the deleted record. |
| 404 | Not Found | No subscriber exists with the specified ID. |

## Example request

```shell
curl --request DELETE "http://localhost:3000/subscribers/5"
```

## Example response

```json
{}
```
