from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_page.urls')),
    path('courier/', include('courier.urls')),
    path('support/', include('support.urls')),
    path('rider/', include('rider.urls')),
    path('scooters/', include('scooters.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
