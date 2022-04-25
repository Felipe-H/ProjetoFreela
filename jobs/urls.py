from . import views
from django.urls import path

#
urlpatterns = [
    path('encontrar_jobs/', views.encontrar_jobs, name="encontrar_jobs")
]

