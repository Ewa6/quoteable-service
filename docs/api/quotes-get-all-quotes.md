---
layout: default
title: Your Page Title
---

# Get all quotes

Returns an array of `quotes` objects that contains all quotes associated with the subscribers.

## URL

```shell
{server_url}/quotes
```

## Params

None

## Request headers

```shell
Content-Type: application/json
```

## Request body

None

## Return body

```js
[
    {
        "subscriberId": 1,
        "id": 3,
        "healthQuoteText": "Good health is not something we can buy. However, it can be an extremely valuable savings account. – Anne Wilson Schaef",
        "loveQuoteText": "",
        "helpPplQuoteText": "At the end, it's not about what you have or even what you've accomplished. It's about who you've lifted up, who you've made better. It's about what you've given back. – Denzel Washington",
        "customQuote": "False",
        "customQuoteText": "",
        "shareQuote": "True",
        "shareQuoteContact": "pepper.pots@stark.com"
    },
    {
        "subscriberId": 2,
        "id": 1,
        "healthQuoteText": "",
        "loveQuoteText": "When we lose someone we love, we must learn not to live without them, but to live with the love they left behind. - Unknown",
        "helpPplQuoteText": "If you're not making someone else's life better, then you're wasting your time. — Will Smith",
        "customQuote": "False",
        "customQuoteText": "",
        "shareQuote": "False",
        "shareQuoteContact": ""
    },
    {
        "subscriberId": 3,
        "id": 5,
        "healthQuoteText": "",
        "loveQuoteText": "There is a little boy inside the man who is my brother… Oh, how I hated that little boy. And how I love him too. — Anna Quindlen",
        "helpPplQuoteText": "",
        "customQuote": "False",
        "customQuoteText": "",
        "shareQuote": "False",
        "shareQuoteContact": ""
    },
    {
        "subscriberId": 4,
        "id": 2,
        "healthQuoteText": "Be bold, be brave enough to be your true self. - Queen Latifah",
        "loveQuoteText": "Because, if you could love someone, and keep loving them, without being loved back . . . then that love had to be real. It hurt too much to be anything else. ― Sarah Cross",
        "helpPplQuoteText": "No one is useless in this world who lightens the burdens of another. ― Charles Dickens",
        "customQuote": "False",
        "customQuoteId": "",
        "customQuoteText": "",
        "shareQuote": "True",
        "shareQuoteContact": "bruce.banner@example.com"
    }
]
```

## Return status

| Status value | Return status | Description |
| ------------- | ----------- | ----------- |
| 200 | Success | Requested data returned successfully |
|  ECONNREFUSED | N/A | Service is offline. Start the service and try again. |
