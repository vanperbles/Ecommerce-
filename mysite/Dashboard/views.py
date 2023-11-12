from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Dashboard(TemplateView):
    template_name = 'Dashboard/index.html'


def Dashboard2(request):
    return render(request, 'Dashboard/see.html')