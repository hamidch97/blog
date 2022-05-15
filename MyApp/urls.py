
from django.conf import settings
from django.conf.urls.static import static
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('membres/', include('membres.urls')),
    path('membres/', include('django.contrib.auth.urls')),

    ] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
