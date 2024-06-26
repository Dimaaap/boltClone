from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from social_django.urls import urlpatterns as social_django_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_page.urls')),
    path('courier/', include('courier.urls')),
    path('support/', include('support.urls')),
    path('rider/', include('rider.urls')),
    path('scooters/', include('scooters.urls')),
    path('driver/', include('driver.urls')),
    path('business/', include('business.urls')),
    path('social-auth/', include('social_django.urls', namespace='social'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
