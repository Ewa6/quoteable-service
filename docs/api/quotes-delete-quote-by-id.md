---
layout: default
title: Delete a quote
---

# Delete a quote

Deletes a quote record.

## Method

<span class="method method--delete">DELETE</span>

## Endpoint

```text
{base_url}/quotes/{id}
```

## Path parameters

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer | Required | Unique quote ID. |

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
| 200 | OK | JSON Server deleted the quote and returned the deleted record. |
| 404 | Not Found | No quote exists with the specified ID. |

## Example request

```shell
curl --request DELETE "http://localhost:3000/quotes/3"
```

## Example response

```json
{}
```
