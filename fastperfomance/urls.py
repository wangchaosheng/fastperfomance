from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='性能平台接口文档', description='xxx描述')),
    path('user/', include('user.urls')),
    path('', include('system.urls')),
    path('', include('interfaces.urls')),
    path('', include('projects.urls')),
    path('', include('interfaces_executive_outcomes.urls')),



]
