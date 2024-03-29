"""
variables I want in results:

'id'
'name'
'price_level'  0 through 4
'rating'
'user_ratings_total'
'vicinity' --like address

gives back a dictionary of lists of dictionaries and now
I am just parsing thorught that
"""

import time
import operator
from GeoCodeLocate import Location


class Filter:

    def __init__(self):
        self.maps = Location()
        self.latitude, self.longitude = self.maps.get_location()
        self.coordinates = str(self.latitude)+","+str(self.longitude)
        self.api_key = self.maps.get_gmaps_key()
        self.places_result = []
        self.descriptions = {}
        self.scores = {}
        self.results_part = []
        self.sorted_scores = []

    def fill_places(self, ranging):

        initial_page = self.api_key.places_nearby(location=self.coordinates,
                                                  radius=ranging,
                                                  open_now=True,
                                                  type='restaurant')
        self.places_result.append(initial_page)
        count = 0

        while 'next_page_token' in self.places_result[count].keys():
            # pprint.pprint(places_result[count]['next_page_token'])

            count = count + 1
            time.sleep(3)
            page = self.places_result[count-1]['next_page_token']
            next_places = self.api_key.places_nearby(page_token=page)
            self.places_result.append(next_places)

        for i in self.places_result:
            self.results_part.extend(i['results'])

    def get_description(self, number):
        # create try catches for every space
        description = self.results_part[number]['name'] + "\n"
        vicinity = self.results_part[number]['vicinity']
        description += "at: " + vicinity + "\n"
        try:
            price_level = self.results_part[number]['price_level']
            price_level = str(price_level)
            description += "price level: " + price_level + "\n"
        except Exception:
            description += "no price level stated\n"
        finally:
            rating = str(self.results_part[number]['rating'])
            description += "has a rating of " + rating + " stars\n"

            total_ratings = self.results_part[number]['user_ratings_total']
            total_ratings = str(total_ratings)
            description += "with " + total_ratings

            if self.results_part[number]['user_ratings_total'] == 1:
                description += str(" review")
            else:
                description += str(" reviews")
            return description

    def get_score(self, number):

        # the price level is a missing value the try catch
        # block will try to account for that
        try:
            useful_price_level = self.results_part[number]['price_level']
        except Exception:
            useful_price_level = 5
        finally:
            amount_ratings = self.results_part[number]['user_ratings_total']
            star_rating = self.results_part[number]['rating']
            score = (amount_ratings * star_rating) / (useful_price_level + 1)
            return score

    def fill_dictionaries(self):
        for i in range(len(self.results_part)):
            identification = self.results_part[i]['id']

            self.descriptions[identification] = self.get_description(i)
            self.scores[identification] = self.get_score(i)

    def print_all_as_sorted(self):
        # sorted score is now a list of tuples
        # sorting based on scores rating formula created
        key1 = operator.itemgetter(1)
        score_items = self.scores.items()
        self.sorted_scores = sorted(score_items, key=key1, reverse=True)
        for i in range(len(self.sorted_scores)):
            identification = self.sorted_scores[i][0]
            count = i + 1
            print(count, ".")
            print(self.descriptions[identification])
            print("has a rating of ", self.sorted_scores[i][1])
            print()

    # this is for food with a price_level of 0
    def only_free_food(self):
        self.scores = {}
        self.descriptions = {}
        self.sorted_scores = []
        results_part2 = []
        for i in range(len(self.results_part)):
            # some don't have price_levels
            try:
                if self.results_part[i]['price_level'] == 0:
                    results_part2.append(self.results_part[i])
            except Exception:
                pass
        if len(results_part2) != 0:
            self.results_part = results_part2
            self.fill_dictionaries()
            self.print_all_as_sorted()
        else:
            message = "There were no restaurants in radius"
            message += " with the price level being 0"
            print(message)

    def rank(self, ranging):

        self.fill_places(ranging)
        self.fill_dictionaries()
        self.print_all_as_sorted()

        return len(self.sorted_scores) != 0


# I used information from this part
# https://www.youtube.com/watch?v=qkSmuquMueA
# where I learned to use operator
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

# https://stackoverflow.com/questions/50704611/next-page-token-google-places
