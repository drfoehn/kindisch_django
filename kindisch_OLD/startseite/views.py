from django.shortcuts import render
from startseite.models import Freizeittipp
# Create your views here.

def index(request):
    return render(request, 'startseite/index.html')

def freizeittipps(request):
    freizeittipp_list = Freizeittipp.objects.order_by('updated_current')
    freizeittipp_dict = {'freizeittipps': freizeittipp_list}
    return render(request, 'startseite/freizeittipps.html', context=freizeittipp_dict)
