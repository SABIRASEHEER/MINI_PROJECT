from django.conf.urls import url
from staff import views

urlpatterns = [
    url('post_staff/', views.post_staff),
    url('view_staff/', views.view_staff)

]