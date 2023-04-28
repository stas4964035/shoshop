import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/read/', adminapp.DealUsersListView.as_view(), name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('countries/read/', adminapp.countries, name='countries'),
    path('countries/create/', adminapp.CountryCreateView.as_view(),
         name='country_create'),
    path('countries/update/<int:pk>/', adminapp.CountryUpdateView,
         name='country_update'),
    path('countries/delete/<int:pk>/', adminapp.CountryDeleteView.as_view(),
         name='country_delete'),
    path('deal/read/countries/<int:pk>/', adminapp.deals,
         name='deals'),
    path('deal/update/<int:pk>/', adminapp.deal_update,
         name='deal_update'),
    path('deal/create/countries/<int:pk>/',
         adminapp.deal_create, name='deal_create'),
    path('deal/read/<int:pk>/',
         adminapp.DealDetailView.as_view(),
         name='deal_read'),
    path('deal/delete/<int:pk>/',
         adminapp.deal_delete, name='deal_delete'),


]
