from django.urls import path

from .views import ProjectListView, ProjectDetailView

project_list = path('projects/', ProjectListView.as_view())
project_detail = path('projects/<int:project_id>/', ProjectDetailView.as_view())
