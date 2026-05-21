---
layout: default
title: Quoteable Service documentation
---

# Quoteable Service documentation

Quoteable Service is a mock API for managing subscribers and the quotes they want to receive. The service is built with JSON Server and is intended for learning, testing, and API documentation practice.

The API has two resources:

* `subscribers`: Stores subscriber contact details, delivery preferences, and quote category preferences.
* `quotes`: Stores quote records associated with subscribers.

## Get started

Prepare your environment, start the mock service, and make your first API request:

* [Prepare your Windows device](tutorials/prepare-windows.md)
* [Prepare your Mac device](tutorials/prepare-mac.md)
* [Quick start guide](tutorials/quick-start-guide.md)

## API reference

Use `{base_url}` for the server URL. When you run the mock API locally, `{base_url}` is:

```text
http://localhost:3000
```

<div class="api-index">

### Subscribers endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/subscribers` | Retrieve all subscribers. |
| <span class="method method--get">GET</span> | `/subscribers/{id}` | Retrieve one subscriber by ID. |
| <span class="method method--post">POST</span> | `/subscribers` | Create a subscriber. |
| <span class="method method--put">PUT</span> | `/subscribers/{id}` | Replace a subscriber. |
| <span class="method method--delete">DELETE</span> | `/subscribers/{id}` | Delete a subscriber. |

See the [`subscribers` resource overview](api/subscribers.md).

### Quotes endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/quotes` | Retrieve all quotes. |
| <span class="method method--get">GET</span> | `/quotes/{id}` | Retrieve one quote by ID. |
| <span class="method method--post">POST</span> | `/quotes` | Create a quote. |
| <span class="method method--put">PUT</span> | `/quotes/{id}` | Replace a quote. |
| <span class="method method--delete">DELETE</span> | `/quotes/{id}` | Delete a quote. |

See the [`quotes` resource overview](api/quotes.md).

</div>

## Tutorials

Use these tutorials to practice common API tasks:

* [Create a subscriber and add their first quote](tutorials/create-subscriber-add-first-quote.md)
* [Retrieve all quotes for a subscriber](tutorials/all-quotes-for-subscriber.md)
* [Update a subscriber's email or mobile number](tutorials/update-email-mobile.md)
* [Update a subscriber's quote preferences](tutorials/update-subscribers-quote-preferences.md)
* [Modify a subscriber's quote frequency](tutorials/modify-quote-frequency.md)
* [Change a subscriber's delivery method](tutorials/change-delivery-method.md)
* [Add a custom quote for a subscriber](tutorials/add-custom-quote-for-subscriber.md)
* [Implement basic error handling](tutorials/implement-error-handling.md)

## Limitations

This project uses JSON Server to simulate an API. It does not include authentication, production validation, rate limits, or a custom backend.
