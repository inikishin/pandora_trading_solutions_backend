import os, sys
sys.path.insert(0, '/var/www/u1016303/data/www/api.pandoratradingsolutions.ru/pandora_trading_solutions_backend')
sys.path.insert(1, '/var/www/u1016303/data/venv_pts_api/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pandora_trading_solutions_backend.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
