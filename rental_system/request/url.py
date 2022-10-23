from django.conf.urls import url
from request import views

urlpatterns = [
    url('post_request/', views.post_request),
    url('view_request/', views.view_request),
    url('viewstatus/',views.viewstatus)


]