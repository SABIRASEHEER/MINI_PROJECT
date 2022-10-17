from django.conf.urls import url
from bike import views


urlpatterns=[
    url('post_bike/', views.post_bike),
    url('view_bike/', views.view_bike),
    url('update/(?P<idd>\w+)', views.update, name='ff'),
    url('delete/(?P<idd>\w+)', views.delete, name='fk')

]