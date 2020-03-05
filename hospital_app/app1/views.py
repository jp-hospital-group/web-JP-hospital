from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from app1.models import App1Hospitalinfo, ViewHospitalInfo


# Create your views here.
def index(request):
    return HttpResponse("hello world!")


class ShowAllHospitalInfo(generic.ListView):
    template_name = 'test_figure.html'
    context_object_name = 'HospitalInfo'

    def get_queryset(self):
        return App1Hospitalinfo.objects.order_by('-bed_number')[0:100]


class ShowTokyoHospitalInfo(generic.ListView):
    template_name = 'test_figure.html'
    context_object_name = 'HospitalInfo'

    def get_queryset(self):
        return ViewHospitalInfo.objects.filter(prefecture_name="東京都").order_by('-bed_number')
