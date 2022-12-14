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
from .views import *
from rest_framework import routers
from django.conf.urls.static import static
from .settings import STATIC_URL



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'circuits', CircuitViewSet)
router.register(r'results', ResultViewSet)
router.register(r'constructors', ConstructorViewSet)
router.register(r'drivers', DriverViewSet)

router2 = routers.DefaultRouter('api/v2')

urlpatterns = [
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    
    re_path('^api/v2/results/(?P<pk>\w+)', ResultDetailApiView.as_view()),
    re_path('^api/v2/circuits/(?P<pk>\w+)', CircuitDetailApiView.as_view()),
    re_path('^api/v2/drivers/(?P<pk>\w+)', DriverDetailApiView.as_view()),
    re_path('^api/v2/constructors/(?P<pk>\w+)', ContructorDetailApiView.as_view()),

    re_path('^api/v2/', include(router.urls)),
    
    re_path('circuits', circuit, name='circuits'),
    re_path('results', result, name='results'),
    
    path("auth/login", login, name="login"),
    path("auth/logout", logout, name="logout"),
    path("auth/callback", callback, name="callback"),
    path('', index, name='index'),
   

] +  static(STATIC_URL)
