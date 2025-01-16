from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from django.utils.dateparse import parse_date
import pandas as pd
from .models import FormSubmission
from .serializers import FormSubmissionSerializer


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
def verify_registration(request):
    cpf = request.data.get('cpf')
    email = request.data.get('email')

    if FormSubmission.objects.filter(cpf=cpf, email=email).exists():
        return Response(
            {"message": "Acesso autorizado! Bem-vindo ao seminário."},
            status=status.HTTP_200_OK
        )

    return Response(
        {"message": "Inscrição não encontrada. Por favor, inscreva-se primeiro."},
        status=status.HTTP_404_NOT_FOUND
    )


def export_forms_to_excel(request):
    """
    Exporta os dados dos formulários para um arquivo Excel.
    O arquivo pode ser filtrado por um intervalo de datas usando os parâmetros GET:
    - start_date: Data inicial no formato YYYY-MM-DD.
    - end_date: Data final no formato YYYY-MM-DD.
    """

    # Filtro opcional por data
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Busca os dados do banco
    forms = FormSubmission.objects.all()

    if start_date:
        forms = forms.filter(submitted_at__gte=parse_date(start_date))
    if end_date:
        forms = forms.filter(submitted_at__lte=parse_date(end_date))

    # Seleciona os campos a serem exportados
    forms = forms.values('nome', 'cpf', 'email', 'comprovante', 'submitted_at')

    # Converte os dados para um DataFrame do pandas
    df = pd.DataFrame(forms)

    # Remove a informação de fuso horário do campo de data e hora
    if 'submitted_at' in df.columns:
        df['submitted_at'] = pd.to_datetime(df['submitted_at']).dt.tz_localize(None)

    # Configura a resposta HTTP para baixar o arquivo
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="relatorio_forms.xlsx"'

    # Cria o arquivo Excel na memória e escreve os dados
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Formulários')

    return response
