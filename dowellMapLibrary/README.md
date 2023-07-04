# Dowell Maps Library Documentation

This library is designed for the [Living-lab-Maps API](https://github.com/DoWellUXLab/Living-Lab-Maps). Through the respective endpoints, you can

1. Verify place IDs
2. Get place details
3. Save place details
4. Get local nearby locations

## Installation

This library currently supports Python 3.6+. The [requests](https://pypi.python.org/pypi/requests) package is required. 

```
pip install dowell-map
```

## Examples

### Verify place IDs

The `verify_place_ids` method takes a list of place IDs and returns the ones not yet saved in the database.

```python
from dowell_map import endpoints

unique_ids = endpoints.verify_place_ids({
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
```

### Get place details

The `get_place_details` method takes a list of place IDs and a dictionary of two lists: `successful_results` and `failed_results`.

```python
from dowell_map import endpoints

place_details = endpoints.get_place_details({
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

```

### Get local nearby locations

The `get_local_nearby_locations` function takes two radii and other location details and returns nearby locations that meet the search criteria.

```python
from dowell_map import endpoints

nearby_locations = endpoints.get_local_nearby_locations({
    "radius1":0,
    "radius2":750,
    "center_lat": 51.50853,
    "center_lon":-0.12574,
    "query_string": "school",
    "data_type": "scraped"
})

print(nearby_locations)
```

### Save place details

Finally, the `save_place_details` function saves place details.

```python
from dowell_map import endpoints

output = endpoints.save_place_details({
        "result_dict": {
            "succesful_results": [
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

print(output)
```