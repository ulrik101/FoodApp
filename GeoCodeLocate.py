import googlemaps
import json
import sys
import codecs
import requests
import responses



gmapsKey = googlemaps.Client(key='AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y')

results = gmapsKey.geolocate()

#accessing individual coords
lat = results["location"]["lat"]
lng = results["location"]["lng"]
coords = (lat,lng)

print("current coordinates")
print(coords)



#JSON TABLE EXAMPLE BELOW
#https://maps.googleapis.com/maps/api/geocode/json?latlng=33.7867326,-117.8428536999999&key=AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y

resultsReverse = gmapsKey.reverse_geocode(coords)


#accessing a variable within json
print("Nearby address")
print(resultsReverse[0]["address_components"][0]["long_name"])