#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    grabs data from remote json feed, inserts/updates local database
    does address lookups on google maps api
    --- --- ---
    on scraperwiki there is a json feed from a scraped website
    website is a listing of all California Wildlife Rehab Facilities
    site lists city and state but no address.

    this script takes the data from that feed and puts it into local database
    then tries to do googlemaps address lookups on each
    --- --- ---
    I would prefer this just be another scraperwiki but I don't see
    a way to put private env vars in scraperwiki (for googlemaps api key)

"""
# scraperwiki url
json_url = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=json&name=california_wildlife_rehab_facilities&query=select+*+from+`swdata`'

# setup for running as shell script
from django.core.management import setup_environ
from rescue_map_project import settings
setup_environ(settings)

# script imports
import time
import urllib2
import json
from googlemaps import GoogleMaps, GoogleMapsError
from django.db import connection
from django.db.utils import IntegrityError
from rescue_map_app.models import Facility
from random import randrange

GOOG_API_KEY = settings.GOOG_API_KEY

class sync_feed:

    tries = 0
    max_tries = 150

    gmaps = GoogleMaps(GOOG_API_KEY)

    def get_data(self, json_url):
        """
            fetch json data from fussy remote url
        """
        try:
            return json.loads(urllib2.urlopen(json_url).read())
        except:
            # couldn't connect to scraperwiki, chill for a few secs and try again
            self.tries = self.tries + 1
            if self.tries < self.max_tries:
                time.sleep(randrange(10))  # wait time is random bt 1-10 seconds
                self.get_data(json_url)
            else:
                import sys
                sys.exit("max tries get_data")

    def search_google_maps(self, search_str):
        """
            send a search string to google maps interface
            returns response
        """
        try:
            loc = self.gmaps.local_search(search_str)
            return loc
        except GoogleMapsError:
        # googlemaps failure usually connection, chill a few secs and try again
            self.tries = self.tries + 1
            if self.tries < self.max_tries:
                time.sleep(randrange(10))
                self.search_google_maps(search_str)
            else:
                import sys
                sys.exit("max tries search_google_maps")

    def find_facility(self, json_place):
        """
            given a place from the data source in json, add or find our model object, returns model obj
        """
        # place = Facility(county="Alameda", city="Hayward", name="Homer Simpson", scraperwiki_id=3)  # this works
        place = Facility(county=json_place["county"], city=json_place["city"], name=json_place["name"], state="CA")

        try:
            place.save()
            print "added new " + ' '.join([json_place["county"], json_place["city"], json_place["name"]])
        except IntegrityError:
            connection._rollback()  # oh hai pgsql
            # print "we all good " + json_place["name"]
            pass

        return Facility.objects.get(city=json_place["city"], name=json_place["name"])

    def update_address(self, place):
        """
            using the name and city lookup the address in googlemaps
            and update the address in model
        """
        loc = self.search_google_maps('"' + str(place.name) + '" ' + str(place.city) + ' ' + 'California')
        place.address = ''
        try:
            place.address = loc[u'responseData']['results'][0][u'streetAddress']
            print "saved new address for " + place.name + "\n " + place.address + "\n" + place.city
        except IndexError:
            print "no address for " + place.name + " in " + place.city
        except TypeError:
            print "no address for " + place.name + " in " + place.city
        place.save()  # address found, save to db


if __name__ == "__main__":

    sf = sync_feed()
    data = sf.get_data(json_url)

    for j in data:
        place = sf.find_facility(j)
        sf.update_address(place)
