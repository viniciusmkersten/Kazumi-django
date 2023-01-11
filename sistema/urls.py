from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.pagina_externa,name='externa'),
    path('', include('cadastro.urls')),
    path('login/', views.entrar_site, name='entrar')
]
