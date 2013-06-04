from django.utils import simplejson
from django.http import HttpResponse
from annoying.decorators import ajax_request
from rescue_map_app.models import Facility

from django.core import serializers

# @ajax_request
def data_dump(request):
    # data = serializers.serialize("json", Facility.objects.all())
    data = list(Facility.objects.all().values('name', 'phone', 'specializations', 'address', 'city', 'county', 'state'))
    return HttpResponse(simplejson.dumps(data),'application/json')
