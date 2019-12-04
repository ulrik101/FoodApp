FROM ubuntu:16.04
FROM python:3.7-alpine

RUN pip3 install --upgrade setuptools

RUN pip3 install googlemaps
WORKDIR /usr/local/bin
RUN cd /usr/local/bin

COPY GeoCodeLocate.py .

COPY RestaurantFilter.py .

COPY RestaurantRanker.py .

CMD python3 RestaurantRanker.py