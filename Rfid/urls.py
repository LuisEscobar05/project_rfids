from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.RfidView.as_view()),
    re_path(r'^(?P<pk>\w+)$', views.RfidDetail.as_view()),
    re_path(r'^(?P<number_rfid>\w+)$', views.RfidDetailNumberRFID.as_view()),
]