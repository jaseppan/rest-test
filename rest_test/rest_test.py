import json
import requests
from generated_content.generator import generated_content

def test_api_endpoint(url, method, parameters, iterations = 1, id_list = []):

    """
    Test an API endpoint with a set of parameters.
    """
    responses = {}

    # If id_list is not empty check that length of id_list equal to iterations 
    if len(id_list) > 0 and len(id_list) != iterations:
        raise Exception("id_list length must equal to iterations")
    
    for i in range(iterations):
        # Generate random values for parameters
        generated_parameters = {}
        for key, value in parameters.items():
            # If value is string
            if isinstance(value, str):
                if value == "%id_num":
                    generated_parameters[key] = id_list[i]
                else:
                    generated_parameters[key] = generated_content(value)
            # Id value is list
            elif isinstance(value, list):
                generated_parameters[key] = []
                for item in value:
                    generated_parameters[key].append(generated_content(item))
            # default
            else:
                generated_parameters[key] = value
        
        # Send request to the API endpoint
        response = requests.request(method, url, json=generated_parameters)

        responses[i] = {
            "url": response.url,
            "status_code": response.status_code,
            "text": response.text
        }
    
    return responses

def get_id(response):
    response_text = response['text']
    parsed_response = json.loads(response_text)

    data = parsed_response.get("data")
    if data:
        nested_data = data.get("data")
        if nested_data:
            id_value = nested_data.get("id")
            if isinstance(id_value, int):
                return id_value

    return None
    
def get_id_list(responses):
    id_list = {}
    for key, response in responses.items():
        id_list[key] = get_id(response)

    return id_list

def test_crud(create_url, read_url, update_url, delete_url, create_parameters, read_parameters, update_parameters, delete_parameters):
    
    crud_responses = {}
    # Test POST 
    method = "POST"
    iterations = 1
    responses = test_api_endpoint(create_url, method, create_parameters)
    crud_responses['create'] = responses
    id_list = get_id_list(responses)

    if( len(id_list) < 1 ) :
        return None
    
    # Test GET
    # method = "GET"
    # responses = test_api_endpoint(read_url, method, read_parameters, 1, id_list)
    # crud_responses['read'] = responses
    
    # Test PUT
    response = test_api_endpoint(update_url, method, update_parameters, 1, id_list)
    crud_responses['update'] = responses
    
    # Test DELETE
    response = test_api_endpoint(update_url, method, update_parameters, 1, id_list)
    crud_responses['delete'] = responses
    
    return crud_responses