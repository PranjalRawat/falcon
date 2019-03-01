from django.conf.urls import url
from Beginner import views
from django.contrib.auth import views as auth_views

app_name = 'Beginner'
urlpatterns =[
        url(r'^beginner/introduction.html/$',views.introduction,name='introduction'),
        url(r'^beginner/environment_setup.html/$',views.environment_setup,name='environment_setup'),
        url(r'^beginner/hello_world.html/$',views.hello_world,name='hello_world'),
        url(r'^beginner/varibles.html/$',views.varibles,name='varibles'),
        url(r'^beginner/numeric.html/$',views.numeric,name='numeric'),
        url(r'^beginner/casting.html/$',views.casting,name='casting'),
        url(r'^beginner/string.html/$',views.string,name='string'),
        url(r'^beginner/operators.html/$',views.operators,name='operators'),
        url(r'^beginner/input_and_output.html/$',views.input_and_output,name='input_and_output'),
        url(r'^beginner/decision_making.html/$',views.decision_making,name='decision_making'),
        url(r'^beginner/list.html/$',views.list,name='list'),
        url(r'^beginner/dictionary.html/$',views.dictionary,name='dictionary'),
        url(r'^beginner/tuple.html/$',views.tuple,name='tuple'),
        url(r'^beginner/sets.html/$',views.sets,name='sets'),
        url(r'^beginner/conditions.html/$',views.conditions,name='conditions'),
        url(r'^beginner/while_loop.html/$',views.while_loop,name='while_loop'),
        url(r'^beginner/for_loop.html/$',views.for_loop,name='for_loop'),
        url(r'^beginner/function.html/$',views.function,name='function'),
        url(r'^beginner/lambda.html/$',views.lambda_,name='lambda_'),
        url(r'^beginner/date_and_time.html/$',views.date_and_time,name='date_and_time'),
]
