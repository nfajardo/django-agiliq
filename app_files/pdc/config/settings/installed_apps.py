
DJANGO_APPS = [
    #'tenant_schemas',  # mandatory, should always be before any django app
    #'apps.tenants',  # you must list the app where your tenant model resides in

    # everything below here is up to your project needs
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'anymail',
]

TENANT_APPS = [
    # Your tenant-specific apps
    'apps.files',
]

LOCAL_APPS = [
    'apps.common',
    'apps.core',
    'apps.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + TENANT_APPS + LOCAL_APPS