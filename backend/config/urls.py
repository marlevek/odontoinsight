"""
URL configuration for OdontoInsight project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('', include('apps.core.urls')),
    path('clinics/', include('apps.clinics.urls')),
    path('procedures/', include('apps.procedures.urls')),
    path('analytics/', include('apps.analytics.urls')),
    path('benchmarking/', include('apps.benchmarking.urls')),
    path('automation/', include('apps.automation.urls')),
    path('reports/', include('apps.reports.urls')),
    
    # API URLs (futuro)
    # path('api/', include('apps.api.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Debug toolbar (only in local)
    if settings.DJANGO_ENV == 'local':
        try:
            import debug_toolbar
            urlpatterns = [
                path('__debug__/', include(debug_toolbar.urls)),
            ] + urlpatterns
        except ImportError:
            pass

# Customize admin
admin.site.site_header = "OdontoInsight Admin"
admin.site.site_title = "OdontoInsight"
admin.site.index_title = "Painel Administrativo"
