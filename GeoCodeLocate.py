import googlemaps
import json
import sys
import codecs
import requests
import responses

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
print(results)



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