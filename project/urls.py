from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.voicetest.urls')),  # Assuming you have an app named 'myapp'
]
