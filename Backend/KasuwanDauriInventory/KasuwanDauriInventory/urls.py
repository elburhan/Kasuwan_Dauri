from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from UserServices.Controller.DynamicFormController import DynamicFormController  # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title="Kasuwan Dauri API",
        default_version='v1',
        description="API documentation for Kasuwan Dauri",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@kasuwan_dauri.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('UserServices.urls')),
    path('api/getForm/<str:modelName>/', DynamicFormController.as_view(), name='dynamicForm'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
