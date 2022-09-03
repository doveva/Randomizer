from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from random import seed, randint
import datetime

class Home(TemplateView):
    template_name = "home.html"


def API(request):
    seed_value = datetime.datetime.utcnow().timestamp()//1
    if seed_value % 10 < 5:
        seed_value = seed_value//10*10
    else:
        seed_value = seed_value//10*10 + 5
    seed(seed_value)
    return HttpResponse(json.dumps({"value": randint(1, 1000000)}), content_type='application/json')
