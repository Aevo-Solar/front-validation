"""
URL configuration for uwb_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('index', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('django/accounts/', include('django.contrib.auth.urls')),
    re_path(r'^favicon\.ico$', favicon_view),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('devices/', include('devices.urls')),
]
