from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Falcon'
urlpatterns =[
        url(r'^$',views.index,name='index'),
        url(r'^login/$',auth_views.LoginView.as_view(template_name='Falcon/login.html'), name='login'),
        url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
        url(r'^signup/$',views.SignUp.as_view(),name='signup'),

]