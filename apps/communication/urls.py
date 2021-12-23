from django.conf.urls import url

from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^request_client/$', views.request_client),
    url(r'^init_boomer/$', views.init_boomer),
    url(r'^shutdown_boomer/$', views.shutdown_boomer),
    url(r'^swarm/$', views.swarm),
]