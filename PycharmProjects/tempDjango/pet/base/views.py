from django.shortcuts import render
from .models import Pet
from .forms import PetForm

def base_home(request):
    base = Pet.objects.all()
    return render(request, 'base/base_home.html', {'base': base})

def create(request):
    error = ''
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверно'


    form = PetForm()

    data = {
        'form':form,
        'error': error
    }

    return render(request, 'base/create.html', data)

