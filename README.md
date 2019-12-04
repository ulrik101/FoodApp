# FoodApp

We made a program that uses Google Maps to help users find a restaurant. People are usually willing to spend more for higher quality food and less for lower quality food. We will use this idea to rank restaurants for people as a ratio of review ratings and prices.  
__Installment Instructions:__

_If you still need to download python3 type:_
> sudo apt install python3

_Install Required Packages/Libraries:_
> pip3 install googlemaps

> pip3 install responses

_To clone the git repository type:_
> git clone https://github.com/ulrik101/FoodApp.git

_To run and compile the code type the following commands._  
> python3 RestaurantRanker.py 

_Other information:_  
ResturantFilter.py returns the results for up to 60 nearby restaurants.  
GeoCodeLocate.py returns the current coordinates.  
RestaurantRanker.py give proper information from the user to the other two .py files  

After that, to use the program input the radius (in meters) around you would that you would like to search  
for restaurants within. Then type yes if you want to see a list of free food rankings. When tested though we never  
found any free food.  

Also to note, if you are a Windows user I recommend that you run it in PowerShell over  
Command Prompt to allow for better scrolling

On Windows 10 Home we could thouroughly test our Dockerfile but it should work like: 
after cloning this repository  
go to it in you docker terminal  
then,  
> docker build .
> docker run .
