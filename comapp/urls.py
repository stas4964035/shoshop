from django.urls import path
import comapp.views as comapp

app_name = 'comapp'

urlpatterns = [
    path('', comapp.companies, name='index'),
    path('company_details/<int:pk>/', comapp.company,
                                                     name='company'),
]
