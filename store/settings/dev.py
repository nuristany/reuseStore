from .common import *


SECRET_KEY = 'django-insecure-b5^iox7!r&^k4bavbr2k4ukg2ot3*fo6)==!3wygr%r_f0^(n9'



DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'reusestore',
        'Host':'localhost',
        'USER': 'root',
        'PASSWORD': 'root',

    }
}