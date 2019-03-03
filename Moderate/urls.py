from django.conf.urls import url
from Moderate import views
from django.contrib.auth import views as auth_views

app_name = 'Moderate'
urlpatterns =[
        url(r'^moderate/modules.html/$',views.modules,name='modules'),
        url(r'^moderate/files_i_o.html/$',views.files_i_o,name='files_i_o'),
        url(r'^moderate/exceptions.html/$',views.exceptions,name='exceptions'),
        url(r'^moderate/exception_handling.html/$',views.exception_handling,name='exception_handling'),
        url(r'^moderate/user_exceptions.html/$',views.user_exceptions,name='user_exceptions'),
        url(r'^moderate/classes_and_objects.html/$',views.classes_and_objects,name='classes_and_objects'),
        url(r'^moderate/inheritance.html/$',views.inheritance,name='inheritance'),
        url(r'^moderate/overloading.html/$',views.overloading,name='overloading'),
        url(r'^moderate/reg_expressions.html/$',views.reg_expressions,name='reg_expressions'),
        url(r'^moderate/iterator.html/$',views.iterator,name='iterator'),

]
