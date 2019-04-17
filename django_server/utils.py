from django.contrib.auth.models import User
import logging


def try_create_admin_user() -> bool:
    n = User.objects.filter(username='admin').count()
    if n == 0:
        User.objects.create_superuser('admin', 'fake@mail.com', 'passwd')
        logging.info('superuser created')
        return True
    logging.info('superuser admin already exists')
    return False
