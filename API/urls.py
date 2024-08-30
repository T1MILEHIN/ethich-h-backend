from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('the_api.urls')),
    path('universal/', include('universal_app.urls')),  # Include universal_app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
