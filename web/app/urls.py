from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('media/', include('mymedia.urls')),
    path('admin/', admin.site.urls),
]
