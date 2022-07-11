from django.urls import path, re_path
from .views import DashBoardView
from apps.core.views import DashBoardView

app_name = "dashboard"

urlpatterns = [
    path('', DashBoardView.as_view(), name='dashboard'),
]
