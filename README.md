# Quoteable Service API documentation

Quoteable Service is a course project API documentation site for a mock JSON Server application. The service stores subscribers and the quotes they want to receive.

This repository is part of an API documentation project for the University of Washington. The application and course scaffold were provided as starting material. My work focused on the API documentation: resource overviews, endpoint reference topics, tutorials, setup instructions, examples, and documentation-site polish.

## Documentation scope

The documentation covers two API resources:

- `subscribers`: subscriber contact information, delivery preferences, and quote categories.
- `quotes`: quote records associated with subscribers.

The docs include:

- API reference pages for common CRUD operations.
- Beginner-friendly setup and quick-start tutorials.
- Postman-oriented examples for testing the mock service.
- A lightweight Jekyll documentation site.

## View the documentation

Start with [the documentation home page](docs/index.md). The API reference is organized by resource:

- [Subscribers resource](docs/api/subscribers.md)
- [Quotes resource](docs/api/quotes.md)

## Known limitations

This is a mock API built with JSON Server. It does not include authentication, production validation, rate limits, persistent database storage, or a custom backend. The documentation describes the behavior of the course project service and the JSON data model in this repository.
