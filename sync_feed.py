"""
    check the scraperwiki source and import new additions
    try to find addresses for any that don't have.
    Runs occasionally on heroku scheduler

    google api search for an address and update those fields too

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

# setup for running as shell script
from rescue_map_project import settings
from django.core.management import setup_environ
setup_environ(settings)

try:
    GOOG_API_KEY = settings.GOOG_API_KEY
except AttributeError:
    try:
        from rescue_map_project.settings_local import *
    except ImportError:
        pass


# script imports
import time
import urllib2
import json
from googlemaps import GoogleMaps
from django.db import connection
from django.db.utils import IntegrityError

from rescue_map_app.models import Facility

gmaps = GoogleMaps(GOOG_API_KEY)

def get_geo_loc(search_str):
    try:
        loc = gmaps.local_search(search_str)
        return loc
    except GoogleMapsError:  # try again
        time.sleep(2)
        get_geo_loc(search_str)

# look for any new additions to our json data feed and put thems in the db
url = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=json&name=california_wildlife_rehab_facilities&query=select+*+from+`swdata`'
try:
    page = json.loads(urllib2.urlopen(url).read())
except:
    import sys
    sys.exit("could not connect to scraperwiki")


for p in page:
    # facility = Facility(county="Alameda", city="Hayward", name="Homer Simpson", scraperwiki_id=3)
    facility = Facility(county=p["county"], city=p["city"], name=p["name"], state="CA")

    try:
        facility.save()
        print "added new " + ' '.join([p["county"], p["city"], p["name"]])
    except IntegrityError:
        connection._rollback()
        print "we all good " + p["name"]
        pass

    fac = Facility.objects.get(city=p["city"], name=p["name"])

    if not facility.address:
        loc = get_geo_loc('"' + str(fac.name) + '" ' + str(fac.city) + ' ' + 'California')
        try:
            fac.address = loc[u'responseData']['results'][0][u'streetAddress']
            fac.save()  # address found, save to db
            print "saved address for " + fac.name + "\n " + fac.address + "\n" + fac.city
        except IndexError:
            print "no address for " + fac.name + " in " + fac.city



