from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('', home, name='home'),
    path('intro/', intro, name='intro'),
    path('work/', work, name='work'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
    path('message', message, name='message')
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)