from django.urls import path
from django.conf.urls import url
from third_app import views

app_name = 'third_app'

urlpatterns = [
    url(r'^other/$', views.relative, name = 'other'),
    path('users/', views.users, name='users'),
    path('success/', views.index, name='index'),
]
