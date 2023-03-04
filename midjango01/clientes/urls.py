from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('clientes/lista', views.lista, name='lista'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
