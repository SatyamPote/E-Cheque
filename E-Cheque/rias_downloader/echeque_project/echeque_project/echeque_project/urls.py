from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cheques/', include('cheques.urls')),
    path('', include('cheques.urls')), # Add this line to handle root URL
]