from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.AlumnoView.as_view()),
    re_path(r'^(?P<pk>\w+)$', views.AlumnoDetail.as_view()),
]