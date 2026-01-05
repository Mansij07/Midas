from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'Budget/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'Budget/login.html', context)