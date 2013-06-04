There is a listing of California Wildlife Rehap Facillities here:
http://www.dfg.ca.gov/wildlife/WIL/rehab/facilities.html

and a scraperwiki that scrapes that page here:
https://scraperwiki.com/scrapers/california_wildlife_rehab_facilities/

I wanna map these.

That website doesn't list any addresses though, just contact info, so sync_feed.py imports to local db that data and then does Google Maps API lookups to find addresses by business name (where available).

Sync_feed.py runs on Heroku Scheduler. Find that data (Facilities with addresses) here:

http://wildliferescue.herokuapp.com/all.json

or

https://scraperwiki.com/scrapers/californa_wildlife_rehap_facilities_with_addresses/

That's it so far..