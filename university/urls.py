from django.urls import path, re_path
from catalog import views as catalog_views
from schedule import views as schedule_views

handler404 = 'catalog.views.not_found'

urlpatterns = [
    # Project 1 (catalog)
    path('', catalog_views.index, name='catalog_index'),
    re_path(r'^info/$', catalog_views.info, name='info'),
    re_path(r'^authors/$', catalog_views.authors, name='authors'),
    re_path(r'^coursess/$', catalog_views.courses, name='coursess'),
    path('course/<int:course_id>/', catalog_views.course_details, name='course_details'),
    path('author/<int:author_id>/', catalog_views.authors_details, name='authors_details'),

    # Project 2 (schedule)
    path('teachers/', schedule_views.index, name='schedule_index'),
    path('teachers/create/', schedule_views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:teacher_id>/', schedule_views.teacher_update, name='teacher_update'),
    path('teachers/delete/<int:teacher_id>/', schedule_views.teacher_delete, name='teacher_delete'),
    path('teachers/<int:teacher_id>/info/', schedule_views.teacher_info, name='teacher_info'),
    path('teachers/<int:teacher_id>/info/update/', schedule_views.teacher_info_update, name='teacher_info_update'),

    path('courses/', schedule_views.courses, name='courses'),
    path('course/create/', schedule_views.create_course, name='create_course'),
    path('course/<int:course_id>/update/', schedule_views.update_course, name='update_course'),
    path('course/<int:course_id>/delete/', schedule_views.delete_course, name='delete_course'),

    path('student_index/', schedule_views.student_index, name='student_index'),
    path('student_create/', schedule_views.student_create, name='student_create'),
    path('student_update/<int:student_id>/', schedule_views.student_update, name='student_update'),
    path('student_delete/<int:student_id>/', schedule_views.student_delete, name='student_delete'),
]
