from django.shortcuts import render, redirect
from .models import Image, character, geo, arch
from .forms import ImageUploadForm, animalUploadForm, carUploadForm, charUploadForm, geoUploadForm, archUploadForm
from .models import animal, car
# Create your views here.
def animals(request):
    data = animal.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

# Create your views here.
def animalUploadView(request):
    if request.method == 'POST':
        form = animalUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal')
    else:
            form = animalUploadForm()
    return render(request, 'upload.html', {'form': form})

def cars(request):
    data = car.objects.all()
    context = {
        'data' : data
    }
    return render(request,"carDisplay.html", context)

def carUploadView(request):
    if request.method == 'POST':
        form = carUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car')
    else:
            form = carUploadForm()
    return render(request, 'upload.html', {'form': form})


def characters(request):
    data = character.objects.all()
    context = {
        'data' : data
    }
    return render(request,"characterDisplay.html", context)

def charUploadView(request):
    if request.method == 'POST':
        form = charUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('character')
    else:
            form = charUploadForm()
    return render(request, 'upload.html', {'form': form})


def geometry(request):
    data = geo.objects.all()
    context = {
        'data' : data
    }
    return render(request,"geometryDisplay.html", context)


def geoUploadView(request):
    if request.method == 'POST':
        form = geoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('geometry')
    else:
            form = geoUploadForm()
    return render(request, 'upload.html', {'form': form})

def architecture(request):
    data = arch.objects.all()
    context = {
        'data' : data
    }
    return render(request,"ArchitectureDisplay.html", context)

def archUploadView(request):
    if request.method == 'POST':
        form = archUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('architecture')
    else:
            form = archUploadForm()
    return render(request, 'upload.html', {'form': form})






