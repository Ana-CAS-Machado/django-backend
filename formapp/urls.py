from django.urls import path
from .views import FormSubmissionView, ReportView

urlpatterns = [
    path('submit/', FormSubmissionView.as_view(), name='submit_form'),
    path('report/', ReportView.as_view(), name='report'),
]
