from django.db import models

class Facility(models.Model):
    county = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=17, null=True, blank=True)
    specializations = models.CharField(max_length=200, null=True, blank=True)
    scraperwiki_id = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        unique_together = (("city", "name"),)