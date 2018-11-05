from django.conf.urls import url

from app import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^index/$', views.index, name='index'),
    url('^market/(\d+)/(\d+)//(\d+)$', views.market, name='market'),
    url('^cart/$', views.cart, name='cart'),
    url('^mine/$', views.mine, name='mine'),
    url('^register/$', views.register, name='register'),
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
    url('^checkaccount/$', views.checkaccount, name='checkaccount'),
]
