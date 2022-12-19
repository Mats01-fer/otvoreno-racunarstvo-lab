"""orf1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from .views import circuit, CircuitViewSet, ResultViewSet, ResultsList,CircuitsList, result, index, ResultDetailApiView
from rest_framework import routers
from django.conf.urls.static import static
from .settings import STATIC_URL





router = routers.DefaultRouter()
router.register(r'circuits', CircuitViewSet)
router.register(r'results', ResultViewSet)

router2 = routers.DefaultRouter('api/v2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    
    re_path('^api/v2/results/(?P<pk>\w+)', ResultDetailApiView.as_view()),

    re_path('^api/v2/', include(router.urls)),
    
    re_path('circuits', circuit, name='circuits'),
    re_path('results', result, name='results'),
    path('', index, name='index'),
   

] +  static(STATIC_URL)
