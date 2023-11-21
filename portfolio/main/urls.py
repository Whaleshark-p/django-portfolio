from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projecten', views.projecten, name="projecten"),
    path('cv', views.cv, name="cv"),
]
