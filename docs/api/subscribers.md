---
layout: page
---

# `subscribers` resource

With the `subscribers` resource you can manage subscriber information in the Quoteable Service. It allows you to:

* Retrieve subscriber details.
* Create new subscribers.
* Update subscriber information.
* Remove subscribers

## Base endpoint

```shell
{server_url}/subscribers
```

## Resource properties

Sample `subscribers` resource

```js
    {
        "id": 1,
        "lastName": "Stark",
        "firstName": "Tony",
        "email": "t.stark@example.com",
        "mobile": "2125551212",
        "healthQuote": "True",
        "loveQuote": "False",
        "helpPplQuote": "True",
        "deliverTo": 1,
        "frequency": 3
    }
```

| Property name | Type | Description | Mandatory |
| ------------- | ----------- | ----------- |     :----:    |
| `id` | integer | The subscriber's unique ID. | :white_check_mark: |
| `lastName` | string | The subscriber's last name. | :white_check_mark: |
| `firstName` | string | The subscriber's first name.  | :white_check_mark: |
| `email` | string | The subscriber's email address.| :white_check_mark: |
| `mobile` | number | The subscriber's mobile phone number. | :x: |
| `healthQuote` | Boolean | Indicates whether the subscriber wants to get a quote from the **Health** category. By default, it's set to `True`. | :white_check_mark:  |
| `loveQuote` | Boolean | Indicates whether the subscriber wants to get a quote from the **Love** category.  | :white_check_mark: |
| `helpPplQuote` | Boolean | Indicates whether the subscriber wants to get a quote from the **Helping People** category.  | :white_check_mark:  |
| `deliverTo` | integer | Indicates whether the user wants to get the quote by email or by text message. | :white_check_mark: |
| `frequency` | integer | How often the subscriber wants to get a quote or quotes. | :white_check_mark: |

## CRUD Operations

See API reference below to see which CRUD actions supports the `subscribers` resource.

### Create (POST)

[Add a new subscriber](subscrinbrs-add-subscriber.md)

### Read (GET)

[Get all subscribers](subscribers-get-all-subscribers.md)

[Get a subscriber by ID](subscribers-get-subscriber-by-id.md)

### Update (PUT/PATCH)

[Update a subscriber by ID](subscribers-update-subscriber.md)

### Delete (DELETE)

[Delete a subscriber by ID](subscribers-delete-subscriber.md)
