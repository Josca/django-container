from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from app import views

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^static', views.index),
    url(r'^write', views.Writer.as_view()),
    url(r'^health', views.Health.as_view()),
    url(r'^swagger', get_swagger_view(title='Django containerized app')),
    url('', include('django_prometheus.urls')),
]
