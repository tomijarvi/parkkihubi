from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from parkings.api.auth import urls as auth_urls
from parkings.api.enforcement import urls as enforcement_urls
from parkings.api.monitoring import urls as monitoring_urls
from parkings.api.operator import urls as operator_urls
from parkings.api.public import urls as public_urls

urlpatterns = [
    url(r'^auth/v1/', include(auth_urls, namespace='auth')),
]

if getattr(settings, 'PARKKIHUBI_PUBLIC_API_ENABLED', False):
    urlpatterns.append(url(r'^public/v1/', include(public_urls, namespace='public')))

if getattr(settings, 'PARKKIHUBI_MONITORING_API_ENABLED', False):
    urlpatterns.append(
        url(r'^monitoring/v1/',
            include(monitoring_urls, namespace='monitoring')))

if getattr(settings, 'PARKKIHUBI_OPERATOR_API_ENABLED', False):
    urlpatterns.append(url(r'^operator/v1/', include(operator_urls, namespace='operator')))

if getattr(settings, 'PARKKIHUBI_ENFORCEMENT_API_ENABLED', False):
    urlpatterns.append(
        url(r'^enforcement/v1/',
            include(enforcement_urls, namespace='enforcement')))

urlpatterns.extend([
    url(r'^admin/', admin.site.urls),
])
