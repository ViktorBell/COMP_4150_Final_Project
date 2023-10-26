"""
URL configuration for Fiction2Form_BackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
cdfrom django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from threeD_model_database_interface_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.model_list, name='model_list'),
    # path('<int:model_id>/', views.model_detail, name='model_detail'),
    # path('upload/', views.model_upload, name='model_upload'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Add paths for update and delete views here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


