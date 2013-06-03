from django.db import models

class Facility(models.Model):
    county = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=17)
    specializations = models.CharField(max_length=200)
    scraperwiki_id = models.IntegerField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=13)

    class Meta:
        unique_together = (("city", "name"),)