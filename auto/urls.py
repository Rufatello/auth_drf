from django.urls import path
from auto.apps import AutoConfig
from auto.views import AutoCreateView, AutoListView, AutoUpdateView, AutoDeleteView

app_name = AutoConfig.name


urlpatterns = [
    path("create/", AutoCreateView.as_view(), name="auto-create"),
    path("list/", AutoListView.as_view(), name="auto=list"),
    path("update/<int:pk>", AutoUpdateView.as_view(), name="auto-update"),
    path('delete/<int:pk>', AutoDeleteView.as_view(), name='auto-delete')
]
