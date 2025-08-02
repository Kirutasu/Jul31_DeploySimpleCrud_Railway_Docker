# En tu urls.py principal del proyecto
from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import redirect # <-- Ya no necesitas esta si usas RedirectView
from django.views.generic.base import RedirectView # <--- ¡Nueva importación!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
            path('libros/', include('libros.urls')),
            path('categorias/', include('categorias.urls')),
    ])),
    # --- Añade esta línea para la redirección de la raíz usando RedirectView ---
    path('', RedirectView.as_view(url='/v1/libros/', permanent=True)),
]