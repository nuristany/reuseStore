
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf .urls.static import static



admin.site.site_header = "Second Hand Shop"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('shop/', include('shop.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

