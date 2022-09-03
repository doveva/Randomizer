from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from random import seed, randint
import datetime

class Home(TemplateView):
    """
    View class that returns HTML to user without any modification
    """
    template_name = "home.html"


def API(request):
    """
    Function to handle generated API call
    :param request: Request from user (in our case JS page)
    :return: JSON string
    """
    seed_value = datetime.datetime.utcnow().timestamp()//1
    if seed_value % 10 < 5:
        seed_value = seed_value//10*10
    else:
        seed_value = seed_value//10*10 + 5
    seed(seed_value)
    return HttpResponse(json.dumps({"value": randint(1, 1000000)}), content_type='application/json')
