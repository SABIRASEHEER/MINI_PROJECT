from django.conf.urls import url
from request import views

urlpatterns = [
    url('post_request/', views.post_request),
    url('view_request/', views.view_request),
    url('viewstatus/',views.viewstatus),
    url('appr/(?P<idd>\w+)', views.approve, name='kk'),
    url('reje/(?P<idd>\w+)', views.reject, name='mm')


]