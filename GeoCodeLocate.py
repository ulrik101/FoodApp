import googlemaps
import json
import sys
import codecs
import requests
import responses

# we will eventualy need to use datetime for
# making sure the restaurants will be open when the user
# is on the app
from datetime import datetime



gmapsKey = googlemaps.Client(key='AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y')
responses.add(responses.POST,
			  'https://www.googleapis.com/geolocation/v1/geolocate',
			  body='{"location": {"lat": 51.0,"lng": -0.1},"accuracy": 1200.4}',
			  status=200,
			  content_type='application/json')


results = gmapsKey.geolocate()

#accessing individual coords
lat = results["location"]["lat"]
lng = results["location"]["lng"]
#print(results)


#JSON TABLE BELOW
#https://maps.googleapis.com/maps/api/geocode/json?latlng=33.7867326,-117.8428536999999&key=AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y
responses.add(responses.GET,
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
content_type='application/json')
resultsReverse = gmapsKey.reverse_geocode((33.7867326,-117.8428536999999))


#accessing a variable within json
print(resultsReverse[0]["address_components"][0]["long_name"])


#my stuff here

# I used information from this part
# https://www.youtube.com/watch?v=qkSmuquMueA


#  range = input('How far would like to search within your current location (in meters): ')

# eventually get rid of the next three lines they are for debugging purposes****
import time
import pprint


range = 700
print(lat)
print(lng)

# I will add a feature later that allows the user to pick to input in their location in km and mi****
# I would also like to include bar and cafe but I can only use one tupe
coordinates = str(lat)+","+str(lng)

# change back to True

places_result = gmapsKey.places_nearby(location = coordinates, radius = range, open_now = False, type = 'restaurant')

x = len(places_result['results'])
print(x)
pprint.pprint(places_result['results'][0].keys())#[i]['name'])

"""
variables I want in results:

'name'
'price_level'  0 through 4
'rating'
'user_ratings_total'
'vicinity' --like address

"""


"""
print(places_result['results'][3]['price_level'])
for i in:
	pprint.pprint(i)
	print("****")
	#pprint.pprint(places_result['results'][i])#['price_level'])#['results'])
"""
"""
#print(places_result)
# I am commenting this out because it will create more GET requests during testing and we don't want to be charged
# time.sleep(3)
# places_result = gmapsKey.places_nearby(page_token = places_result('next_page_token'))

 

#don't forget to flake8 this program
"""

