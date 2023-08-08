from django.shortcuts import render
from .models import ThreeDModel
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import ThreeDModelForm


# Create your views here.

# List View: Display all 3D Models in the database
def model_list(request):
    models = ThreeDModel.objects.all()
    return render(request, 'threeD_model_database_interface_app/model_list.html', {'models': models})


# Detail View: Displays detailed information about a specific 3D model, including its associated auxiliary models.

def model_detail(request, model_id):
    model = get_object_or_404(ThreeDModel, id=model_id)
    aux_models = model.auxiliary_models.all()
    return render(request, 'threeD_model_database_interface_app/model_detail.html', {'model': model, 'aux_models': aux_models})

# Upload View: Allows users to upload a 3D model. They can also choose to upload auxiliary models at the same time.
# This easily allows users to upload 'multi-piece' models without needing to go through the hassle of individual associating the aux models



def model_upload(request):
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            # If auxiliary models are uploaded, handle them here
            # For simplicity, we're redirecting to the list view
            return redirect('model_list')
    else:
        form = ThreeDModelForm()
    return render(request, 'threeD_model_database_interface_app/model_upload.html', {'form': form})

def model_upload(request):
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES)
        if form.is_valid():
            main_model = form.save()

            # Check if auxiliary models are uploaded
            aux_models_files = request.FILES.getlist('aux_models_files')
            for aux_file in aux_models_files:
                aux_model = ThreeDModel(main_model_file=aux_file)
                aux_model.save()
                main_model.auxiliary_models.add(aux_model)

            return redirect('model_list')
    else:
        form = ThreeDModelForm()
    return render(request, 'threeD_model_database_interface_app/model_upload.html', {'form': form})


# Update View: Allows users to update the details of a 3D model, including associating it with auxiliary models.
# For the case when a user creates and uploads a base model and then at a later date creates auxiliary models for it and uploads them separately
def model_update(request):
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            # If auxiliary models are uploaded, handle them here
            # For simplicity, we're redirecting to the list view
            return redirect('model_list')
    else:
        form = ThreeDModelForm()
    return render(request, 'threeD_model_database_interface_app/model_upload.html', {'form': form})


# Delete View: Allows users to delete a 3D model.
def model_delete(request, model_id):
    model = get_object_or_404(ThreeDModel, id=model_id)
    model.delete()
    return redirect('model_list')
