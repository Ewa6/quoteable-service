# Quoteable Service documentation

Quoteable Service is a mock API for managing subscribers and the quotes they want to receive. The service is built with JSON Server and is intended for learning, testing, and API documentation practice.

The API has two resources:

* `subscribers`: Stores subscriber contact details, delivery preferences, and quote category preferences.
* `quotes`: Stores quote records associated with subscribers.

## Get started

Follow the instructions in these topics to prepare your environment and get started:

* [Prepare your Windows device]({{ site.baseurl }}/docs/tutorials/prepare-windows.html)
* [Prepare your Mac device]({{ site.baseurl }}/docs/tutorials/prepare-mac.html)
* [Quick start guide]({{ site.baseurl }}/docs/tutorials/quick-start-guide.html)

## API reference

Use `{base_url}` for the server URL. When you run the mock API locally, `{base_url}` is:

```text
http://localhost:3000
```

<div class="api-index" markdown="1">

### Subscribers endpoints

The following table lists endpoints for the `subscribers` resource.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/subscribers` | Retrieve all subscribers. |
| <span class="method method--get">GET</span> | `/subscribers/{id}` | Retrieve one subscriber by ID. |
| <span class="method method--post">POST</span> | `/subscribers` | Create a subscriber. |
| <span class="method method--patch">PATCH</span> | `/subscribers/{id}` | Update part of a subscriber. |
| <span class="method method--put">PUT</span> | `/subscribers/{id}` | Replace a subscriber. |
| <span class="method method--delete">DELETE</span> | `/subscribers/{id}` | Delete a subscriber. |

For details on the subscribers resource, see the [`subscribers` resource overview]({{ site.baseurl }}/docs/api/subscribers.html).

### Quotes endpoints

The following table lists endpoints for the `quotes` resource.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| <span class="method method--get">GET</span> | `/quotes` | Retrieve all quotes. |
| <span class="method method--get">GET</span> | `/quotes/{id}` | Retrieve one quote by ID. |
| <span class="method method--post">POST</span> | `/quotes` | Create a quote. |
| <span class="method method--patch">PATCH</span> | `/quotes/{id}` | Update part of a quote. |
| <span class="method method--put">PUT</span> | `/quotes/{id}` | Replace a quote. |
| <span class="method method--delete">DELETE</span> | `/quotes/{id}` | Delete a quote. |

For details on the quotes resource, see the [`quotes` resource overview]({{ site.baseurl }}/docs/api/quotes.html).

</div>

## Tutorials

Follow these tutorials to practice common API tasks:

* [Create a subscriber and add their first quote]({{ site.baseurl }}/docs/tutorials/create-subscriber-add-first-quote.html)
* [Add a custom quote for a subscriber]({{ site.baseurl }}/docs/tutorials/add-custom-quote-for-subscriber.html)
* [Update a subscriber's email or mobile number]({{ site.baseurl }}/docs/tutorials/update-email-mobile.html)
* [Update a subscriber's quote preferences]({{ site.baseurl }}/docs/tutorials/update-subscribers-quote-preferences.html)
* [Modify a subscriber's quote frequency]({{ site.baseurl }}/docs/tutorials/modify-quote-frequency.html)
* [Change a subscriber's quote delivery method]({{ site.baseurl }}/docs/tutorials/change-delivery-method.html)
* [Retrieve all quotes for a subscriber]({{ site.baseurl }}/docs/tutorials/all-quotes-for-subscriber.html)
* [Implement basic error handling]({{ site.baseurl }}/docs/tutorials/implement-error-handling.html)

## Limitations

This project uses JSON Server to simulate an API. It does not include authentication, production validation, rate limits, or a custom backend.
