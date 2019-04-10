from django.urls import path
from . import views
app_name = "wheredoyoulive"
urlpatterns = [
    path('', views.index, name='index'),
    path('make_user', views.make, name='make'),
    path('users', views.show_users, name='show_users'),
]
