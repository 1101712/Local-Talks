from django.shortcuts import render
from django.views.generic import ListView
from .models import Ad
from django.http import HttpResponse

class AdListView(ListView):
    model = Ad
    template_name = 'talks/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 10

def test_view(request):
    return HttpResponse("Test Page")