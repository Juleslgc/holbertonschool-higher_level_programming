# Project - Understanding HTTP, HTTPS & Using cURL

## Task 0: Basic Web Concepts

### Differences between HTTP and HTTPS

| Protocol | Default Port | Encryption | SSL Certificate | Typical Use Case                   |
|----------|--------------|------------|-----------------|----------------------------------|
| HTTP     | 80           |  No      |  No           | Non-sensitive websites           |
| HTTPS    | 443          |  Yes     |  Required     | Payments, secure logins          |

HTTPS protects data by encrypting it via TLS/SSL, unlike HTTP which sends data in plain text.

---

### 📤 Structure of an HTTP Request and Response

#### Example HTTP Request
```
http
GET /page HTTP/1.1
Host: example.com
User-Agent: curl/7.81.0
Accept: */*
```

#### Example HTTP Response
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 305

<html>...</html>
```
- A request contains: method + path + headers + (optional) body
- A response contains: status code + headers + body

### Common HTTP Methods

| Method | Description          | Example Use Case              |
| ------ | -------------------- | ----------------------------- |
| GET    | Retrieves a resource | Reading a webpage or API data |
| POST   | Creates a resource   | Submitting a form             |
| PUT    | Updates a resource   | Modifying a record            |
| DELETE | Deletes a resource   | Removing an account           |

### Common HTTP Status Codes

| Code | Meaning      | Example Scenario                     |
| ---- | ------------ | ------------------------------------ |
| 200  | OK           | Successful request                   |
| 201  | Created      | Resource created (e.g. POST request) |
| 400  | Bad Request  | Invalid request (missing parameters) |
| 401  | Unauthorized | Authentication required              |
| 404  | Not Found    | Resource not found                   |

## Task 1: Using CURL

### Verify cURL Installation

```
curl --version
```
Returns version info and supported protocols.

### Fetch Webpage Content

```
curl http://example.com
```

Displays the HTML content of example.com.

### Fetch Data from a JSON API

```
curl https://jsonplaceholder.typicode.com/posts
```

Returns a JSON array of posts, each with attributes like `userId`, `id`, `title`, and `body`:

```
[
  {
    "userId": 1,
    "id": 1,
    "title": "example title",
    "body": "example body"
  },
  ...
]
```

### Fetch Only Headers

```
curl -I https://jsonplaceholder.typicode.com/posts
```
Returns HTTP headers like:
```
HTTP/1.1 200 OK
Content-Type: application/json
...
```

### Make a Simulated POST Request

```
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
Response (simulated creation):
```
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```
JSONPlaceholder simulates the creation but does not persist data.