from niomic.models import Dreamreal
from django.http import HttpResponse

# Create your views here.
def datamanipulation(request):
    res = ''

    # Filtering Data:
    qs = Dreamreal.objects.filter(name = "Alfabank Jogja")
    res += "Found: %s results<br>" %len(qs)

    # Ordering Data
    qs = Dreamreal.objects.order_by("name")

    for elt in qs:
        res += elt.name + '<br>'

    return HttpResponse(res)