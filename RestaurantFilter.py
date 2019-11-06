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

#this filei is so I don't messup GeoCodeLocate.py