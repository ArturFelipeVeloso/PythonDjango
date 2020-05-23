import os

# Recupera a URL de capitura que o django está rodando
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Usado para fazer uma chave de criptografia das suas senhas e algumas outras coisas
SECRET_KEY = ')%a#n*%15s1ru%1p1!po_&)c&&52ej$e=m&aqw^!h9xf6^s8kk'

# Mantém o django no modo de debug, na hora de subir para o servidor, deixar False
DEBUG = True

# Quais os endereços que sua aplicação vai aceitar ser acessado
# Exemplo: 'www.meusite.com.br'
ALLOWED_HOSTS = []


# Applicações instaladas no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website'
]

# O que o django já trás de segurança, seções, ou seja, principais ferramentas que o django já tem
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configurar a URL principal do seu projeto
ROOT_URLCONF = 'BlogPython.urls'

# Configurações de templates HTML, CSS e JS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do seu WSGI
WSGI_APPLICATION = 'BlogPython.wsgi.application'


# Configuração do seu banco de dados, já com um BD SQLite3 como padrão
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# O DJango já vem com alguns validadores de senha
# Senhas com atributos iguais
# Senhas com tamanho mínimo
# senhas comuns
# senhas somente com valores numericos
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de internacionalizações do Django
# Idioma
LANGUAGE_CODE = 'pt-br'
# Zona
TIME_ZONE = 'America/Sao_Paulo'

# Abilita se vai querer usar ou não o Time Zone
# Muitas línguas
# Muitos paises
USE_I18N = True
USE_L10N = True
USE_TZ = True

# URL onde o Django vai buscar os Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'