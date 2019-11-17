from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.AsistenciaView.as_view()),
    re_path(r'^(?P<pk>\w+)$', views.AsistenciaDetail.as_view()),
]