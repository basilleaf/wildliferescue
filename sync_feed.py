#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    check the scraperwiki source and import any changes
    try to find addresses for any that don't have.
    Runs on heroku scheduler
"""
from rescue_map_app.models import *
