from django.contrib import admin
from django.urls import path, include
#app_name = 'tasks'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),  # Añadido
]
