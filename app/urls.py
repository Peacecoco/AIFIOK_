from django.urls import path
from .views import index,about,contact,faq,service,success_view

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('service', service, name='service'),
    path('faq', faq, name='faq'),   
    path('success/', success_view, name='success'),
]