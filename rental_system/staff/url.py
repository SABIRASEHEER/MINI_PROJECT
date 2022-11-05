from django.conf.urls import url
from staff import views

urlpatterns = [
    url('post_staff/', views.post_staff),
    url('view_staff/', views.view_staff),
    url('update/(?P<idd>\w+)', views.update, name='ff'),
    url('delete/(?P<idd>\w+)', views.delete, name='fk')

]