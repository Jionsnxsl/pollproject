from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^productinfo$', views.ProductInfoView, name="productinfo"),
    url(r'^testpagechange/$', views.Test_changepage, name="testpagechange"),
    url(r'^testpagechangeone/', views.Test_changepage_one, name="testpagechangeone"),
    url(r'^testpagechangetwo/', views.Test_changepage_two, name="testpagechangetwo"),
    url(r'^datatable/', views.datatable, name="datatable"),
    url(r'^userinfo/$', views.userInfo, name="userInfo"),
]

