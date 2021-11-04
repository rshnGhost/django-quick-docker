from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('dataStorage.urls')),
	path('accounts/',include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
