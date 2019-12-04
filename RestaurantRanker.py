from RestaurantFilter import Filter

ranker = Filter()
rangeString = "What is the range you would like to view"
rangeString += " restaurants within (in meters)? "
ranging = input(rangeString)


# typecast to int
while not ranging.isdigit():
    print("You didn\'t input a number try again")
    ranging = input(rangeString)
ranging = int(ranging)

# the api key only goes to 10000 and sometimes if the
# user put in ridiculous high numbers google maps will
# not know what to do

if ranging > 10000:
    ranging = 10000

any_restaurants = ranker.rank(ranging)

if not any_restaurants:
    print("There were no restaurants in the area specified")
else:
    messageString = "Would you like to find food"
    messageString += " from the previous group of"
    messageString += " restaurants with the lowest"
    messageString += " price level possible being 0"
    messageString += " (type \'yes\' to see)? "
    choice = input(messageString)
    if choice == "yes":
        ranker.only_free_food()
    else:
        print("bye")
