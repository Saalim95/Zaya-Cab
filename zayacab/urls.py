from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/register', views.RegisterUser.as_view()),
    url(r'^driver/register', views.RegisterDriver.as_view()),
    url(r'^user/(?P<commuter_id>[0-9]+)/history', views.TripHistoryUser),
    url(r'^driver/(?P<driver_id>[0-9]+)/history/', views.TripHistoryDriver),
    url(r'^driver/available', views.DiversAvailable), 
    url(r'^user/location/(?P<commuter_id>[0-9]+)', views.UserLocation),
    url(r'^update/(?P<driver_id>[0-9]+)', views.ChangeStatus),
    url(r'^booking/(?P<commuter_id>[0-9]+)/(?P<driver_id>[0-9]+)', views.BookCab),
]

urlpatterns = format_suffix_patterns(urlpatterns)