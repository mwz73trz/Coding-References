from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('subjects', views.get_subject_list, name='get_subject_list'),
    path('<int:subject_id>', views.get_subject_detail, name='get_subject_detail'),
    path('new_subject', views.new_subject, name='new_subject'),
    path('<int:subject_id>/edit', views.edit_subject, name='edit_subject'),
    path('<int:subject_id>/delete', views.delete_subject, name='delete_subject'),

]