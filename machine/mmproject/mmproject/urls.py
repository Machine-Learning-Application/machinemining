"""mmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import articles
from articles import views
from articles.views import HelloTemplate
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',articles.views.home),
    url(r'^hello/$', articles.views.hello),
    url(r'^hello_template/$', articles.views.hello_template),
    url(r'^hello_template_simple/$', articles.views.hello_template_simple),
    url(r'^HelloTemplate/$', HelloTemplate.as_view()),
    #url(r'^articles/',include('articles.urls')),
]
