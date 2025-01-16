from rest_framework import serializers
from .models import FormSubmission

class FormSubmissionSerializer(serializers.ModelSerializer):
    comprovante = serializers.FileField(required=False)

    class Meta:
        model = FormSubmission
        fields = ['nome', 'cpf', 'email', 'comprovante']

    def validate_nome(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Nome deve ser uma string válida.")
        return value

    def validate_cpf(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("CPF deve ser uma string válida.")
        return value

    def validate_email(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Email deve ser uma string válida.")
        return value

    def validate_comprovante(self, value):
        # Verifica se o arquivo é do tipo PDF
        if value and not value.name.endswith('.pdf'):
            raise serializers.ValidationError("O arquivo deve ser no formato PDF.")
        return value
