from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    # sample of sending
    a = 3
    context = {'': a}
    return render(request, "index.html", context)
