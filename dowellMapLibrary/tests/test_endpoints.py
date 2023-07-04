from dowell_map import endpoints
import pytest
import json

def test_verify_place_ids():
    output = endpoints.verify_place_ids({
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
    
    expected_output = {'unique_ids':['EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0EiGhIYChQKEgnRTo6ixx-qiRHo_bbmkCm7ZRAN','IhoSGAoUChIJ0U6OoscfqokR6P225pApu2UQDQ','EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0E']}
    
    assert eval(output) == expected_output
    
    

def test_save_place_details():
    output = endpoints.save_place_details({
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
    
    assert output == '"Saved Succesfully"'
    
    

def test_get_local_nearby_locations():
    output = endpoints.get_local_nearby_locations({
        "radius1":0,
        "radius2":750,
        "center_lat": 51.50853,
        "center_lon":-0.12574,
        "query_string": "school",
        "data_type": "scraped"
    })
    
    expected_output = {"data":[{"location_coord":"51.511709 , -0.1344253","hav_distances":697.3070865942444,"category":["primary_school","school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJm3x5cdMEdkgRVY_WzPEVcjA","place_name":"Soho Parish Primary School"},{"location_coord":"51.5134615 , -0.1192713","hav_distances":707.8811283949044,"category":["primary_school","school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJtVFJ6soEdkgRFa3NDt6VCiE","place_name":"St Clement Danes Church of England Primary School"},{"location_coord":"51.5129392 , -0.1250222","hav_distances":492.7914239010622,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJ7elx8swEdkgRRxhEjmqMnfQ","place_name":"Czech School without Borders"},{"location_coord":"51.5149056 , -0.1235464","hav_distances":725.0058918771838,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJMVEJicAFdkgRYgTnvQ2dvCw","place_name":"Dexterity Global Academy"},{"location_coord":"51.5149037 , -0.1235842","hav_distances":724.2559519547087,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJ76tTBLkFdkgRf2XouprHvFs","place_name":"The ACE School of Success"},{"location_coord":"51.5074424 , -0.1332092","hav_distances":530.8896125020152,"category":["primary_school","school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJwebhG9EEdkgRaRxoPjHeL-s","place_name":"Cavendish Education"},{"location_coord":"51.5101173 , -0.1218421","hav_distances":322.37012142927153,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJ__bF1nAFdkgR2sq3U_Sbbhs","place_name":"Harrow School Online"},{"location_coord":"51.510729 , -0.1264515","hav_distances":249.426589053067,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJ3fiby80EdkgRt9ppEBur39c","place_name":"The London School of Figure Drawing"},{"location_coord":"51.5074596 , -0.1332842","hav_distances":535.5166570807756,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJXwlqGdEEdkgRJExl2IE2Kpw","place_name":"Dukes Education"},{"location_coord":"51.5100814 , -0.1219658","hav_distances":313.0237956888915,"category":["school","point_of_interest","establishment"],"placeId":"None","place_id":"ChIJYXBKtOfleUgRDNRTa-yTFpQ","place_name":"Pearson Online Academy UK Global"},{"location_coord":"51.512019 , -0.134288","hav_distances":707.4324194024349,"category":["school","point_of_interest","establishment"],"placeId":"ChIJj41Ng9MEdkgRmtC5YiBVwEc","place_id":"None","place_name":"LEYF - Soho Nursery & Pre-School"},{"location_coord":"51.5142 , -0.1299","hav_distances":693.0932953574444,"category":["school","point_of_interest","establishment"],"placeId":"ChIJU58L08MFdkgRGZDtNcjtnGQ","place_id":"None","place_name":"Saint Martin Art School"}]}
    
    assert json.loads(output) == expected_output