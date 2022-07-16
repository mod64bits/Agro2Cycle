# Agro2Cycle

### Verificando versão do Python 
python --version

### Verificando versão do Django
>>> import django
>>> print(django.get_version())

### Setup

a) Instalando pré-requisitos
pip install -r requirements.txt -f (??? não funcionou, tive que instalar um a um, cada item do arquivo requirements.txt)
python -m pip install Pillow

b) Criando o banco de dados
python manage.py migrate

### Executando a aplicação

python manage.py runserver localhost:8000
