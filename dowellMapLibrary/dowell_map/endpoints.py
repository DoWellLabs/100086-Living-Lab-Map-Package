def verify_place_ids(payload):
    """
    Does any of provided IDs exist in the database? 
    Return only the IDs that do not exist in the database.
    """
    
    import requests
    url = "https://100086.pythonanywhere.com/accounts/verify-place-ids/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text




def get_place_details(payload):
    """
    Send the verified IDs to this endpoint. 
    The endpoint returns the most important details for display or saving. The response is divided into:
    1. successful_results - successful queries
    2. failed_results - queries that resulted in errors.
    """
    
    import requests
    url = "https://100086.pythonanywhere.com/accounts/get-details-list-stage1/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text




def save_place_details(payload):
    """ 
    Save the place details in readiness for later use.
    """
    
    import requests
    url = "https://100086.pythonanywhere.com/accounts/save-places-detail/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text




def get_local_nearby_locations(payload):
    """ 
    Retrieve locations from the Dowell database that meet certain criteria specified in the payload. 
    Among the details include two radii, that determine the distance range. 
    The endpoint returns the locations falling within the range.
    """
    
    import requests
    url = "https://100086.pythonanywhere.com/accounts/get-local-nearby/"
    headers = {}
    response = requests.post(url, headers=headers, json=payload)
    return response.text

