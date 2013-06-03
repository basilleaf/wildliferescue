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

# script imports
import urllib2
import json
from django.db.utils import DatabaseError
from rescue_map_app.models import Facility

url = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=json&name=california_wildlife_rehab_facilities&query=select+*+from+`swdata`'
page = json.loads(urllib2.urlopen(url).read())

for p in page:
    # facility = Facility(county="Alameda", city="Hayward", name="Homer Simpson", scraperwiki_id=3)
    facility = Facility(county=p["county"], city=p["city"], name=p["name"])

    try:
        facility.save()
        print "added new " + ' '.join([p["county"], p["city"], p["name"]])
    except DatabaseError:
        print "we all good " + p["name"]
        pass


