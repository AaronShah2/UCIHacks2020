from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
# Create your views here.
class LoginView(View):
    def get(self, request):
        a = 3 / 10
        context = {'a': a}
        return render(request, "boss/index.html", context)

def main(request):
    # sample of sending
    a = 3 / 10
    context = {'a': a}
    return render(request, "boss/index.html", context)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # if form is valid, saves user to the database
        if form.is_valid():
            form.saved()
            return redirect('/home')
    else:
        # if the form is not valid, tells user what they did wrong
        form = UserCreationForm()
        args = {"form": form}
        return render(request, "boss/reg_form.html", args)