from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect # <--- ¡Cambiado!


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
            path('libros/', include('libros.urls')),
            path('categorias/', include('categorias.urls')),
    ])),
    # --- Añade esta línea para redirigir la raíz ---
    path('', redirect('/v1/libros/', permanent=True)), # Redirige la raíz a /v1/libros/
]