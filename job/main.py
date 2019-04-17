import os
import django
import datetime
import pytz

# this way we can use django orm out-of-the-box even in job code
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_server.settings'
django.setup()

from app.models import Sample


def show_samples():
    # TODO: do something with data

    # testing insert some values
    Sample.objects.create(timestamp=datetime.datetime.now(tz=pytz.UTC), value=1.1)
    Sample.objects.create(timestamp=datetime.datetime.now(tz=pytz.UTC), value=2.2)

    # and show them
    samples = Sample.objects.all()
    for sample in samples:
        print(sample)


if __name__ == '__main__':
    show_samples()
