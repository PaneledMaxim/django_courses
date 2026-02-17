from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^info', views.info, name='info'),
    re_path(r'^authors',
            views.authors,
            kwargs={'Family': 'Pushkin', 'Name': "Alexander"},
            name='authors'),
]
