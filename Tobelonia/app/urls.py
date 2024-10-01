from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index.as_view(), name="index"),  
    path('settings/', views.Settings.as_view(), name="settings"),  
    path('services/', views.Services.as_view(), name="services"),  
    path('pricing/', views.Pricing.as_view(), name="pricing"),  
    path('contacts/', views.Contact.as_view(), name="contacts"),  
]