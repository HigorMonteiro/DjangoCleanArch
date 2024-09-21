import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['seu-dominio.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
