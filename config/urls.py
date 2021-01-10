from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App1.urls', namespace='App1')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
]

# static # media
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
