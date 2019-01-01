from django.conf.urls import include, url
from rest_framework import routers
from parking import views

# 定义路由地址
# route = routers.DefaultRouter()

# 注册新的路由地址
# route.register(r'login', views.api_login)

# 注册上一级的路由地址并添加
urlpatterns = [
    url(r'^apilogin/$', views.api_login),
    url(r'^apiregister/$', views.api_register),
]