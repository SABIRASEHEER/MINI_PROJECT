from django.conf.urls import url
from user import views

urlpatterns = [
    url('post_user/', views.post_user),
    url('view_user/', views.view_user)

]