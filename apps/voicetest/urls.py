from django.urls import path
from .views import voice_test_view

urlpatterns = [
    path('', voice_test_view, name='voice_test'),
]
