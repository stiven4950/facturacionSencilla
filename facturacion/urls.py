# Predefined packages
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# Custom packages
from core.urls import core_patterns
from product.urls import product_patterns

urlpatterns = [
    # PATHS core
    path('', include(core_patterns)),
    path('admin/', admin.site.urls),

    
    # Paths AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    # Paths product
    path('', include(product_patterns))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
