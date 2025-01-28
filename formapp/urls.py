from django.urls import path
from .views import FormSubmissionView, ReportView, verify_registration, export_forms_to_excel

urlpatterns = [
    path('submit/', FormSubmissionView.as_view(), name='submit_form'),
    path('report/', ReportView.as_view(), name='report'),
    path('verify/', verify_registration, name='verify_registration'),
    path('export/excel/', export_forms_to_excel, name='export_forms_to_excel'),
]
