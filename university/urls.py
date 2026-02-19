from django.urls import path, re_path
from catalog import views

handler404 = 'catalog.views.not_found'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^info/$', views.info, name='info'),
    re_path(r'^authors/$', views.authors, name='authors'),
    re_path(r'^courses/$', views.courses, name='courses'),

    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('author/<int:author_id>/', views.authors_details, name='authors_details'),
]
