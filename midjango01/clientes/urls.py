from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('clientes/lista', views.lista, name='lista'),
    path('clientes/eliminar/<int:idr>', views.eliminar, name='eliminar'),
    path('clientes/add', views.crear, name='crear'),
    path('clientes/editar/<int:idr>', views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
