#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    check the scraperwiki source and import any changes
    try to find addresses for any that don't have.
    Runs on heroku scheduler
"""
from rescue_map_project import settings
from django.core.management import setup_environ
setup_environ(settings)

from rescue_map_app.models import *

place = Facility(county="Alameda", city="Hayward", name="Homer Simpson", scraperwiki_id=3)
place.save()
