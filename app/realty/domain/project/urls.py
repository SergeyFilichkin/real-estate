from django.urls import path

from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:project_id>/', ProjectDetailView.as_view())
]
