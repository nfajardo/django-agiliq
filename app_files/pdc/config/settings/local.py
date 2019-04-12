from .base import * 
from .installed_apps import *

DEBUG = True

DOMAIN = "http://localhost:8000"

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_ADMINS = ['iris9112@gmail.com', ]

"""
DATABASES = {
    'default': {
        # Use the tenant_schemas specific postgresql_backend
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'test_pdc',
        'USER': 'admin',
        'PASSWORD': 'datatres',
        'HOST': 'localhost',
        'PORT': 5433,
    }
}

# We need to provide this DATABASE_ROUTER in order to get the apps synced to the
# correct schema
DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

"""