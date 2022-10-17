from django.conf.urls import url
from payment import views

urlpatterns = [
    url('post_payment/', views.post_payment),
    url('view_payment/', views.view_payment)

]