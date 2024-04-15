from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('empresas.urls')),
    path('membros/', include ('membros.urls')),
    path('tarefas/', include ('tarefas.urls')),
    path('accounts/', include('contas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
