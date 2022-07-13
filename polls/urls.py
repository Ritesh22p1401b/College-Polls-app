from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('gateway/',include('gateway.urls')),
    path('gateway/',include('django.contrib.auth.urls')),
]
