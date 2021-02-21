from django.shortcuts import render, get_object_or_404
from freizeittipp.models import Freizeittipp
from freizeittipp.forms import NewTippForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def freizeittipps(request):
    freizeittipp_list = Freizeittipp.objects.order_by('updated_current')
    freizeittipp_dict = {'freizeittipps': freizeittipp_list}
    return render(request, 'freizeittipps.html', context=freizeittipp_dict)


def freizeittipp_detail(request, id):
    freizeittipp_detail = get_object_or_404(Freizeittipp, id=id)
    freizeittipp_detail_dict = {'freizeittipps': freizeittipp_detail}
    return render(request, 'freizeittipp_detail.html', context=freizeittipp_detail_dict)


def freizeittipp_add(request):
    form = NewTippForm()
    if request.method == 'POST':
        form = NewTippForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Ungültige Eingabe')
    return render(request, 'freizeittipp_add.html', {'form':form})
