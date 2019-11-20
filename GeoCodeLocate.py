import googlemaps
import json
import sys
import codecs
import requests
import responses


class Location:
	def __init__(self):
		self.gmapsKey = googlemaps.Client(key='AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y')
		self.results = self.gmapsKey.geolocate()
	def getLocation(self):
		#accessing individual coords
		lat = self.results["location"]["lat"]
		lng = self.results["location"]["lng"]
		coords = (lat,lng)

		return coords
coord1=Location()
test=coord1.getLocation()
print(coord1.getLocation())

#JSON TABLE EXAMPLE BELOW
#https://maps.googleapis.com/maps/api/geocode/json?latlng=33.7867326,-117.8428536999999&key=AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y

#resultsReverse = gmapsKey.reverse_geocode(coords)


#accessing a variable within json
#print("Nearby address")
#print(resultsReverse[0]["address_components"][0]["long_name"])