"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
#上面这行多加了一个re_path
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
#导入配置文件里的文件上传配置
from myBlog import views

from django.conf.urls.static import static

from blog.settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),# 管理后台
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    path('', views.index,name='index'),
    #把原来的views.hello修改成views.index  ''留空，表示为首页
    path('list-<int:lid>.html',views.list,name='list'),# 列表页
    path('show-<int:sid>.html',views.show,name='show'),# 内容页
    path('tag/<tag>',views.tag,name='tag'), # 标签列表页
    path('s/',views.search,name='search'), # 搜索列表页
    path('about/',views.about,name='about'), # 关于我们的页面
    path(r'mdeditor/', include('mdeditor.urls')),
    # re_path('static/(?P.*)', serve, {'document_root': STATIC_ROOT}),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)