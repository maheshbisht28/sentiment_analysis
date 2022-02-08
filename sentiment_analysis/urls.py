"""sentiment_analysis URL Configuration

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
from analysis import views 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('sentiment_result/',views.sentiment_result,name='sentiment_result'),
    url('sentiment_results/',views.sentiment_results,name='sentiment_results'),
    url('type/',views.type,name="type"),
    url('types/',views.types,name="types"),
    url('test/',views.test,name="test"),
    url('hasshh/',views.hasshh,name="hasshh"),
    url('sentiment/',views.sentiment,name="sentiment"),
    url('',views.test_sent,name="test_sent"),
    # url('',views.home,name="home"),

]
