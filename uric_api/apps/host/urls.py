from django.urls import path, include, re_path
from host import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.HostModelViewSet.as_view({"get": "list", "post": "create"})),
    re_path('(?P<pk>\d+)', views.HostModelViewSet.as_view({"get": "retrieve", "delete": "destroy"})),

    path('category', views.HostCategoryListAPIView.as_view()),
    path('excel_host', views.HostExcelView.as_view()),

]