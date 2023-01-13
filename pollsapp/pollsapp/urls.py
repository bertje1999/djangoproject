from django.urls import path, include

urlpatterns = [
    path('', include('pollsapp_app.urls')),
]