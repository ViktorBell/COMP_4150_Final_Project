from django.urls import path
from .import views

urlpatterns = [
    path('', views.animals, name='index'),
    path('animal_image/', views.animals, name='animal'),
    path('animalUpload_image/', views.animalUploadView, name='animalUpload_image'),
    path('car_image/', views.cars, name='car'),
    path('carUpload_image/', views.carUploadView, name='carUpload_image'),
    path('character_image/', views.characters, name='character'),
    path('charUpload_image/', views.charUploadView, name='charUpload_image'),
    path('geometry_image/', views.geometry, name='geometry'),
    path('geoUpload_image/', views.geoUploadView, name='geoUpload_image'),
    path('architecture_image/', views.architecture, name='architecture'),
    path('archUpload_image/', views.archUploadView, name='archUpload_image')
]