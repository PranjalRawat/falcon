from django.conf.urls import url
from Advanced import views
from django.contrib.auth import views as auth_views

app_name = 'Advanced'
urlpatterns =[
        url(r'^advanced/system_programming.html/$',views.system_programming,name='system_programming'),
        url(r'^advanced/graph_theory.html/$',views.graph_theory,name='graph_theory'),
        url(r'^advanced/polynomial_manipulation.html/$',views.polynomial_manipulation,name='polynomial_manipulation'),
        url(r'^advanced/linguistics.html/$',views.linguistics,name='linguistics'),
        url(r'^advanced/numerical_computations.html/$',views.numerical_computations,name='numerical_computations'),
        url(r'^advanced/creating_musical_scores.html/$',views.creating_musical_scores,name='creating_musical_scores'),
        url(r'^advanced/databases.html/$',views.databases,name='databases'),
        url(r'^advanced/generator_protocol.html/$',views.generator_protocol,name='generator_protocol'),
        url(r'^advanced/iterator_protocol.html/$',views.iterator_protocol,name='iterator_protocol'),
        url(r'^advanced/meta_programming.html/$',views.meta_programming,name='meta_programming'),
        url(r'^advanced/wsgi_protocol.html/$',views.wsgi_protocol,name='wsgi_protocol'),
        url(r'^advanced/context_managers.html/$',views.context_managers,name='context_managers'),
        url(r'^advanced/design_patterns.html/$',views.design_patterns,name='design_patterns'),

]
