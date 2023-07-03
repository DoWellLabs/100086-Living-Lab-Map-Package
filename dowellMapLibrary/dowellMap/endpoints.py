def verify_place_ids(payload):
    import requests
    url = "https://100086.pythonanywhere.com/accounts/verify-place-ids/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

""" Example
unique_ids = verify_place_ids({
    "place_id_list": [
        "ChIJj3S0t1IbLxgRYgL-7uH0NIo",
        "ChIJrTLr-GyuEmsRBfy61i59si0",
        "ChIJA5TnPS3nGBURRqRffftcUrk",
        "ChIJgUbEo8cfqokR5lP9_Wh_DaM",
        "GhIJQWDl0CIeQUARxks3icF8U8A",
        "EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0EiGhIYChQKEgnRTo6ixx-qiRHo_bbmkCm7ZRAN",
        "EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0E",
        "IhoSGAoUChIJ0U6OoscfqokR6P225pApu2UQDQ"
    ]
})

print(unique_ids)
"""






def get_place_details(payload):
    import requests
    url = "https://100086.pythonanywhere.com/accounts/get-details-list-stage1/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

""" Example
place_details = get_place_details({
    "place_id_list":[
        "ChIJH-YvVNtjhxcRBKtosJMZigI",
        "ChIJsUIT2etjhxcRpvvxvXinMMM",
        "ChIJB_0xDeUZLxgRZDlv3RP72CY",
        "ChIJh75PpvIeLxgRaPu-_UdT9i4",
        "ChIJ7VT_aMwWLxgRIUerCmXISKM",
        "ChIJVVVV5XomLxgRgEK1BB2YarcVMHP+VQ8"
    ]
})

print(place_details)
"""







def save_place_details(payload):
    import requests
    url = "https://100086.pythonanywhere.com/accounts/save-places-detail/"
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

""" Example
result = save_place_details({
        "result_dict": {
            "succesful_results": [
                {
                    "place_id": "ChIJj3S0t1IbLxgRYgL-7uH0NIo",
                    "place_name": "Whitefield Restaurant",
                    "category": [
                        "restaurant",
                        "food",
                        "point_of_interest",
                        "establishment"
                    ],
                    "address": "kingara Road, opp kingara close behind Junction Mall, Nairobi, Kenya",
                    "location_coord": "-1.2960063 , 36.7616708",
                    "day_hours": [
                        "Monday: 11:00 AM -9:00 PM",
                        "Tuesday: 11:00 AM -9:00 PM",
                        "Wednesday: 11:00 AM -9:00 PM",
                        "Thursday: 11:00 AM -9:00 PM",
                        "Friday: 11:00 AM -9:00PM",
                        "Saturday: 11:00 AM -9:00 PM",
                        "Sunday: 11:00 AM -9:00 PM"
                    ],
                    "phone": "+254 742 894700",
                    "website": "https://whitefieldrestaurant.reserveport.com/",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                },
                {
                    "place_id": "ChIJrTLr-GyuEmsRBfy61i59si0",
                    "place_name": "Australian Cruise Group",
                    "category": [
                        "travel_agency",
                        "restaurant",
                        "food",
                        "point_of_interest",
                        "establishment"
                    ],
                    "address": "32 The Promenade, 5 King St, Sydney NSW 2000, Australia",
                    "location_coord": "-33.8676569 , 151.2017213",
                    "day_hours": "None",
                    "phone": "+61 2 8296 7351",
                    "website": "https://www.australiancruisegroup.com.au/",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                },
                {
                    "place_id": "ChIJA5TnPS3nGBURRqRffftcUrk",
                    "place_name": "Dar Al-Hikmah School",
                    "category": [
                        "school",
                        "point_of_interest",
                        "establishment"
                    ],
                    "address": "Dar Alhikma School, Damascus, Syria",
                    "location_coord": "33.5098448 , 36.2973479",
                    "day_hours": "None",
                    "phone": "+963 11 225 9477",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                },
                {
                    "place_id": "ChIJgUbEo8cfqokR5lP9_Wh_DaM",
                    "place_name": "13 Market St",
                    "category": [
                        "street_address"
                    ],
                    "address": "13 Market St, Wilmington, NC 28401, USA",
                    "location_coord": "34.23544330000001 , -77.94935509999999",
                    "day_hours": "None",
                    "phone": "None",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                },
                {
                    "place_id": "GhIJQWDl0CIeQUARxks3icF8U8A",
                    "place_name": "63P2+57 Wilmington",
                    "category": [
                        "plus_code"
                    ],
                    "address": "63P2+57 Wilmington, NC, USA",
                    "location_coord": "34.2354375 , -77.94931249999999",
                    "day_hours": "None",
                    "phone": "None",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                },
                {
                    "place_id": "ChIJgUbEo8cfqokR5lP9_Wh_DaM",
                    "place_name": "13 Market St",
                    "category": [
                        "street_address"
                    ],
                    "address": "13 Market St, Wilmington, NC 28401, USA",
                    "location_coord": "34.23544330000001 , -77.94935509999999",
                    "day_hours": "None",
                    "phone": "None",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": False
                }
            ],
            "failed_results": [
                {
                    "place_id": "EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0EiGhIYChQKEgnRTo6ixx-qiRHo_bbmkCm7ZRAN",
                    "place_name": "None",
                    "category": "None",
                    "address": "None",
                    "location_coord": "None , None",
                    "day_hours": "None",
                    "phone": "None",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": True
                },
                {
                    "place_id": "IhoSGAoUChIJ0U6OoscfqokR6P225pApu2UQDQ",
                    "place_name": "None",
                    "category": "None",
                    "address": "None",
                    "location_coord": "None , None",
                    "day_hours": "None",
                    "phone": "None",
                    "website": "None",
                    "type_of_data": "scraped",
                    "is_test_data": True,
                    "eventId": [
                        "FB1010000000000000000000003004"
                    ],
                    "error": True
                }
            ]
        }
    })

print(result)
"""








def get_local_nearby_locations(payload):
    import requests
    url = "https://100086.pythonanywhere.com/accounts/get-local-nearby/"
    headers = {}
    response = requests.post(url, headers=headers, json=payload)
    return response.text

""" Example
result = get_local_nearby_locations({
    "radius1":0,
    "radius2":750,
    "center_lat": 51.50853,
    "center_lon":-0.12574,
    "query_string": "school",
    "data_type": "scraped"
})

print(result)
"""



