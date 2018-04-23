from django.urls import path
from django.conf.urls import url
from form_app import views

app_name = 'form_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^formpage/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'special/', views.special, name='special'),
    url(r'^user_login/$', views.user_login, name='user_login')
]
