from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FormSubmission
from .serializers import FormSubmissionSerializer

class FormSubmissionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dados enviados com sucesso!"}, status=200)
        return Response(serializer.errors, status=400)


class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        submissions = FormSubmission.objects.all().values()
        return Response(list(submissions))
