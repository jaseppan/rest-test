# Python Module: rest_test
## Description
rest_test is a Python module designed to test REST API endpoints and assist in creating and manipulating test data. It can simulate multiple requests, generate random content for testing, and more.

## Installation
To install the rest_test module:

```arduino
pip install git+https://github.com/jaseppan/rest-test
```

## Dependencies:

**dynamic-content-generator:** A module created by me that provides capabilities to generate dynamic content for testing purposes. 

See: [https://github.com/jaseppan/dynamic_content_generator](https://github.com/jaseppan/dynamic_content_generator)

## Usage
### Testing an API Endpoint
To test an API endpoint:

```python
from rest_test import test_api_endpoint
responses = test_api_endpoint(url, method, parameters, iterations, id_list)

```
Where:

- **url**: The endpoint URL.
- **method**: The HTTP method (e.g., "GET", "POST", "PUT", "DELETE").
- **parameters**: A dictionary containing the parameters to be sent with the request.
- **iterations (optional)**: Number of times to send the request. Default is 1.
- **id_list (optional)**: A list of IDs to be used in the request.

### Retrieving an ID from a Response
To extract an ID from an API response:

```python
from rest_test import get_id

id_value = get_id(response)
```

## Retrieving IDs from Multiple Responses
To extract IDs from multiple API responses:

```python
from rest_test import get_id_list

ids = get_id_list(responses)
```

### Testing CRUD Operations on an API
To test Create, Read, Update, and Delete (CRUD) operations on an API:

```python
from rest_test import test_crud

responses = test_crud(create_url, read_url, update_url, delete_url, create_parameters, read_parameters, update_parameters, delete_parameters)
```

### Author
Janne Seppänen📧 j.v.seppanen@gmail.com