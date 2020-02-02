from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from boss.forms import SignUpForm
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('month')
    else:
        form = UserCreationForm()
    return render(request, 'boss/reg_form.html',{'form': form})
def login(request):
    if request.method == "POST":
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'boss/login.html', {'form': form})
def mainAcc(request):
    return render(request, 'boss/mainAcc.html')