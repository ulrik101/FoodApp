from RestaurantFilter import Filter

ranker = Filter()
ranging = int(input("What is the range you would like to view restaurants within (in meters)? "))
any_restaurants = ranker.rank(ranging)

if not any_restaurants:
    print("There were no restaurants in the area specified")
else:
    choice = input("Would you like to find food from the previous group of restaurants with the lowest price level possible being 0 (type \'yes\' to see)? ")
    if choice == "yes":
        ranker.only_free_food()
    else:
        print("bye")
