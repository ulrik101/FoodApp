import googlemaps
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
# print(resultsReverse[0]["address_components"][0]["long_name"])

#my stuff here

# I used information from this part
# https://www.youtube.com/watch?v=qkSmuquMueA


#  range = input('How far would like to search within your current location (in meters): ')

# eventually get rid of the next three lines they are for debugging purposes****
import time
import pprint
import operator


# print(lat)
# print(lng)

ranging = int(input("What is the range you would like to view restaurants within (in meters)? "))
# I will add a feature later that allows the user to pick to input in their location in km and mi****
# I would also like to include bar and cafe but I can only use one tupe
coordinates = str(lat)+","+str(lng)

# change back to True

places_result = gmapsKey.places_nearby(location = coordinates, radius = ranging, open_now = True, type = 'restaurant')

"""
variables I want in results:

'id'
'name'
'price_level'  0 through 4
'rating'
'user_ratings_total'
'vicinity' --like address

"""

# gives back a dictionary of lists of dictionaries and now I am just parsing thorught that

# print(str(places_result['results'][i]['price_level']))

# print(places_result['results'][1]['price_level'])

# print([3]['price_level'])

# place_id uniquely identifies a place can be used for dicitonary
results_part = places_result['results']

#print(results_part[0].keys())
#print(results_part[0]['id'])
#print(type(results_part[0]['id']))


def get_description (restaurant_number):
    
    #create try catches for every space 
    description = results_part[restaurant_number]['name'] + "\n"
    
    description += "at: " + results_part[restaurant_number]['vicinity'] + "\n"

    try:
        description += "price level: " + str(results_part[restaurant_number]['price_level']) + "\n"
    except:
        description += "no price level stated\n"
    finally:
        description += "has a rating of " + str(results_part[restaurant_number]['rating']) + " stars\n"
        
        description += "with " + str(results_part[restaurant_number]['user_ratings_total']) + " reviews"
        
        return description

def get_score (restaurant_number):

    # the price level is a missing value the try catch block will try to account for that 
    
    try:
        useful_price_level = results_part[restaurant_number]['price_level']
    except:
        useful_price_level = 5
    finally:
        amount_ratings = results_part[restaurant_number]['user_ratings_total']
        star_rating = results_part[restaurant_number]['rating']
        score = (amount_ratings * star_rating) / (useful_price_level + 1)
        return score
    

    #pprint.pprint(places_result['results'][i])#['price_level'])#['results'])


# print(places_result)
# I am commenting this out because it will create more GET requests during testing and we don't want to be charged
# time.sleep(3)
# places_result = gmapsKey.places_nearby(page_token = places_result('next_page_token'))

# print(results_part[0].keys())

#connects the id
descriptions = {}
scores = {}


# print(len(results_part))
for i in range(len(results_part)):
    
    identification = results_part[i]['id']

    descriptions[identification] = get_description(i)
    scores[identification] = get_score(i)



    # print(i)
    # pprint.pprint(results_part[i])
    # print(get_description(i),"\n") 

# sorting based on scores rating formula created


# print(get_description(8))
# print(get_score(8))
# pprint.pprint(results_part[8])

# where I learned to use operator
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# print(type(scores))
sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))

# print(sorted_scores[0][0])

"""
print(sorted_scores.keys())
for i in sorted_scores.keys():
    print(sorted_scores[i])
"""
# pprint.pprint(sorted_scores)

for i in range(len(sorted_scores)):
    identification = sorted_scores[i][0]

    count = i + 1
    print(count,".")
    print(descriptions[identification])
    print("has a rating of ", sorted_scores[i][1])
    print()

#don't forget to flake8 this program

#this filei is so I don't messup GeoCodeLocate.py

# don't forget to Flake8
# for the last part last part lets do the price_level == 0
