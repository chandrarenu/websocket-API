from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ws/', include('attendance.routing.websocket_urlpatterns')),
]
