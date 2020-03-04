from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from app1.models import HospitalInfo


# Create your views here.
def index(request):
    return HttpResponse("hello world!")


class ShowAllHospitalInfo(generic.ListView):
    template_name = 'test_figure.html'
    context_object_name = 'HospitalInfo'

    def get_queryset(self):
        return HospitalInfo.objects.order_by('-bed_number')[0:100]


class ShowTokyoHospitalInfo(generic.ListView):
    template_name = 'test_figure.html'
    context_object_name = 'HospitalInfo'

    def get_queryset(self):
        return HospitalInfo.objects.order_by('-bed_number')[0:100]