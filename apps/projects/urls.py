from rest_framework.routers import SimpleRouter, DefaultRouter
from projects import views
# 定义路由对象
router = SimpleRouter()
router.register(r'projects', views.ProjectsViewSets)

urlpatterns = [
]
# 使用路由对象.urls属性来获取自动生成的路由条码，往往为列表，需要将这个列表添加至urlpatterns
urlpatterns += router.urls
