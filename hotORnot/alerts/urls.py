from django.conf.urls import url

from . import views

app_name = 'alerts'
urlpatterns = [
               url(r'^inner', views.inner, name="inner"),
               url(r'^alert_two', views.alert_two, name="alert_two"),
               url(r'^next', views.next, name="next"),
               url(r'^over', views.over, name="over"),
    ]
