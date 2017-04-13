from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^rent/(?P<item_id>[0-9]+)/$', views.rent, name='rent'),
    url(r'^return_item/(?P<item_id>[0-9]+)/$', views.return_item, name='return_item')

]