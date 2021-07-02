from django.contrib import admin
from django.urls import path

from exam.views import ExamDetailView, ExamCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', ExamDetailView.as_view),
    path('exam/create/', ExamCreateView.as_view),
]
