---
layout: default
title: Make your first request
---

# Make your first request

Welcome to Quoteable Service. This guide walks you through the basic steps to get started with the API to manage subscribers and their favorite quotes.

## Prerequisites

Before you send your first API test call, make sure Node.js, Postman, and GitHub Desktop are installed.

To prepare your operating system, follow these instructions:

- [Prepare your Windows device](prepare-windows.html)
- [Prepare your Mac device](prepare-mac.html)

## Step 1: Fork the Quoteable Service repository

1. Visit the Quoteable Service GitHub repository: <https://github.com/Ewa6/quoteable-service>
2. Select **Fork**, and then select **Create a new fork**. This creates a fork of the Quoteable Service repository in your GitHub account.

## Step 2: Clone the Quoteable Service repository

Once you have forked the repository, you can clone it and work with it. To do so, follow these steps:

1. Open GitHub Desktop.
2. Sign in to your GitHub account.
3. In the upper left corner, select **File** > **Clone Repository**.
4. In the **Clone Repository** dialog, go to the **GitHub.com** tab and select the **quoteable-service** repository.
5. Select **Clone**. After GitHub Desktop clones the repository, you can find it in the specified local directory.

## Step 3: Install project dependencies

Install the project dependencies before you start JSON Server. The project uses a local JSON Server dependency, so you do not need to install JSON Server globally.

1. On Windows, open Command Prompt. On macOS, open Terminal.
2. Navigate to the directory where you cloned the Quoteable Service repository. For example: `cd C:\path\to\your\directory`
3. Run the following command:

```shell
npm install
```

## Step 4: Start JSON Server

To start JSON Server in the directory of your cloned repository, follow these steps:

1. Open a command prompt (cmd) on Windows or a terminal on your Mac.
2. Navigate to the directory where you cloned the Quoteable Service repository. For example: `cd C:\path\to\your\directory`
3. Start JSON Server:

```shell
npm run start:api
```

You can also run the helper scripts from the `quoteable-service-api` directory:

Windows:

```shell
start-server.bat
```

macOS:

```shell
sh start-server.sh
```

JSON Server runs at `http://localhost:3000`. You can test it by opening this address in your web browser.

## Step 5: Make your first API call in Postman

To make your first API call to Quoteable Service, follow these steps:

1. Open Postman.
2. Select the `GET` method and enter the address: `http://localhost:3000/subscribers`.
3. Select **Send**. The response status is `200 OK`, and the response body returns all Quoteable Service subscribers.

```shell
curl "http://localhost:3000/subscribers"
```

![The first call to the Quoteable Service in Postman](../images/postman-first-call-to-quoteable-service.png)

## Next steps

Now that you have a basic understanding of how to use the Quoteable Service, you can explore the API reference for the [`subscribers` resource](../api/subscribers.html) and [`quotes` resource](../api/quotes.html). These topics introduce more detailed information on each endpoint, including request and response formats, error handling, and additional parameters.


<!-- If you need more examples and practice with the Quoteable Service, see our [tutorials] -->

Contact the support team if you have questions or need help.
