from django.conf.urls import url

from app import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^index/$', views.index, name='index'),
    url('^market/$', views.market, name='market'),
    url('^cart/$', views.cart, name='cart'),
    url('^mine/$', views.mine, name='mine'),
]
