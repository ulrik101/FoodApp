import googlemaps


class Location:
    def __init__(self):
        passkey = 'AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y'
        self.gmaps_key = googlemaps.Client(key=passkey)
        self.results = self.gmaps_key.geolocate()

    def get_location(self):
        # accessing individual coords
        lat = self.results["location"]["lat"]
        lng = self.results["location"]["lng"]
        coords = (lat, lng)
        return coords

    def get_gmaps_key(self):
        return self.gmaps_key


"""
coord1=Location()
test=coord1.get_location()
print(coord1.get_location())

"""
# JSON TABLE EXAMPLE BELOW
# https://maps.googleapis.com/maps/api/geocode/json?latlng=33.7867326,-117.8428536999999&key=AIzaSyAt0viCrbReQdXUR00mG4DPWucra5_xx8Y

# resultsReverse = gmapsKey.reverse_geocode(coords)


# accessing a variable within json
# print("Nearby address")
# print(resultsReverse[0]["address_components"][0]["long_name"])
