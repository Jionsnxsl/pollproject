from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    # url(r'^login/', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', logout, {'template_name': 'users/logout.html'}, name='logout'),
]
