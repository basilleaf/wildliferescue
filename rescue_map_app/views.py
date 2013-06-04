from django.utils import simplejson
from django.http import HttpResponse
from annoying.decorators import ajax_request
from rescue_map_app.models import Facility

from django.core import serializers

@ajax_request  # returns dict in json
def data_dump(request):
    return list(Facility.objects.all().values('name', 'phone', 'specializations', 'address', 'city', 'county', 'state'))