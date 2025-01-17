from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    # Above maps any URLs that begin with 'rango/' to be handled by rango
    path('admin/', admin.site.urls),
]
