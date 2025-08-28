from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import portfolio_home

urlpatterns = [
    path('', portfolio_home, name='portfolio_home'),  # Página principal
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)