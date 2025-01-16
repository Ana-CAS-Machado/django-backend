from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import FormSubmission
from .serializers import FormSubmissionSerializer
from rest_framework.decorators import api_view

class FormSubmissionView(APIView):
    def post(self, request):
        serializer = FormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        submissions = FormSubmission.objects.all()
        serializer = FormSubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def submit_form(request):
    print(request.FILES)  # Verifica se o arquivo está sendo enviado
    serializer = FormSubmissionSerializer(data=request.data, files=request.FILES)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Formulário enviado com sucesso!"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

