import os
import django
from django.contrib.auth import get_user_model

# Verifica se a chave de segurança está configurada
SECURITY_KEY = os.getenv('SUPERUSER_SECURITY_KEY')

if SECURITY_KEY != 'mysecretkey':  # Substitua 'mysecretkey' por algo mais seguro
    print("Chave de segurança incorreta. Abortando a criação do superusuário.")
    exit()

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# Obtém o modelo User
User = get_user_model()

# Verifica se já existe um superusuário, caso contrário, cria um
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='codata@prefeitura.sp.gov.br',
        password='DevSePeP@!1'
    )
    print("Superuser criado com sucesso.")
else:
    print("Superuser já existe.")

