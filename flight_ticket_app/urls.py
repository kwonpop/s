from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('download_image/', views.download_image, name='download_image'),
    path('get_image/', views.get_image, name='get_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)