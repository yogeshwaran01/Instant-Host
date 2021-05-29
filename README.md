# Instant-Host

[![Python application](https://github.com/yogeshwaran01/Instant-Host/actions/workflows/python-app.yml/badge.svg)](https://github.com/yogeshwaran01/Instant-Host/actions/workflows/python-app.yml)

Host static pages and Files from your Terminal. It can host your HTML, JSON, XML, and many non-binary files. All hosted files are encrypted and compressed.

## Installation

```bash
$ pip install instanthost
```

## Usage

Usage of Instanthost is very simple

### Host new page

![Demo](./assets/demo.gif)

```bash

instanthost ~/path/to/file

```

Output is like this

```
✌️  Hosted Successfully ✨

created_at: 05/16/2021, 16:39:56

hosted_at: http://instant-host.herokuapp.com/render/U4uhdM4

mimetype: application/xml

private_key: U4uhdM4bnovt

public_key: U4uhdM4

tiny_url: https://tinyurl.com/yehcy54n
```

### Editing the existing page

You can change the data in the file without causing any issues to link with the secret private key. Store your private key for editing content.

```bash
instanthost ~/path/to/new/file --edit --key <your-private-key>
```

Output is

```
✌️  Hosted Successfully ✨

hosted_at: http://instant-host.herokuapp.com/render/U4uhdM4

mimetype: application/xml

private_key: U4uhdM4bnovt

public_key: U4uhdM4

updated_at: 05/16/2021, 16:43:34

tiny_url: https://tinyurl.com/yehcy54n
```

### Delete the existing page

```bash
instanthost delete --key <your-private-key>
```

Like this you can host all non-binary type file from your terminal

you can host your simple static web page, blog post and etc ..
