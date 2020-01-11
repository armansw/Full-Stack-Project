release: python leadmanager/manage.py migrate
web: gunicorn --pythonpath leadmanager/leadmanager leadmanager.wsgi --log-file -