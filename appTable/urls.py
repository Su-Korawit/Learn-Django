from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablepage, name='tablepage'),
    path('<int:grade>', views.changeTablePage, name='changeTablePage'),
]