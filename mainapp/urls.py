from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.deals, name='index'),
    path('deal_details/<int:pk>/', mainapp.deal,
                                                     name='deal'),
]
