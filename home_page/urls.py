from django.conf.urls import url, include
from home_page import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    # url(r'^about_us/$', views.about_us_view, name='about_us'),
]