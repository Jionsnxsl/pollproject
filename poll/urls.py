from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
    url(r'^homepage/$', views.homepage, name="homepage"),
    url(r'^searchbox/$', views.search_box, name="search_box"),
    url(r'^verticaltimeline/$', views.vertical_timeline, name="vertical_timeline"),
    url(r'^btndown/$', views.btn_down, name="btn_down"),
    url(r'^mobiledesign/$', views.mobileDesign, name="mobiledesign"),
    url(r'^generateqrcode/(?P<pid>\d+)$', views.GenerateQRCode, name="generateqrcode"),
    url(r'^uploadimg/$', views.upload_image, name="upload_image"),
    url(r'^showimg/$', views.show_img, name="show_img"),
]

