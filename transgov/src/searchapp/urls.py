"""searchapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main_search.views import HomeView, MeetingView, FacetedSearchView, autocomplete
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^meeting/(?P<slug>[\w-]+)/$', MeetingView.as_view(), name='meeting'),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^find/', FacetedSearchView.as_view(), name='haystack_search'),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)