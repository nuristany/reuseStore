from .common import *


SECRET_KEY = 'django-insecure-b5^iox7!r&^k4bavbr2k4ukg2ot3*fo6)==!3wygr%r_f0^(n9'



DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'reusestore',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'reusestore',
#         'Host':'localhost',
#         'USER': 'root',
#         'PASSWORD': 'root',

#     }
# }