# databases 
DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'yEPRQqztgto5fknd2yB0',
        'HOST': 'containers-us-west-70.railway.app',
        'PORT': '5942',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f!(7@aoc*o^)n*@408_3kk*4732*9ajz=nhks=2yld08-jw5#r'