from django.conf.urls import url
from bike import views


urlpatterns=[
    url('post_bike/', views.post_bike),
    url('view_bike/', views.view_bike),
    url('view_user/', views.view_user),
    url('update/(?P<idd>\w+)', views.update, name='update'),
    url('delete/(?P<idd>\w+)', views.delete, name='delete'),
    # url('Rent/(?P<idd>\w+)', views.Rent, name='fg')


]