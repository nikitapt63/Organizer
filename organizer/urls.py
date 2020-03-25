from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', include('registration.urls')),
    url('main/', include('clock.urls')),
    url('task_list/', include('todo.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

