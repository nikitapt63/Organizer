from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('', views.RegisterFormView.as_view()),
]
