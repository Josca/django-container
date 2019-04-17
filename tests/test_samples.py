from django.test import TestCase
from django.core import serializers
from app.models import Sample
import datetime
import pytz


class Job(TestCase):

    def setUp(self):
        Sample.objects.all().delete()

    def test_1_create(self):

        Sample.objects.create(timestamp=datetime.datetime.now(tz=pytz.UTC), value=1)

        self.assertEqual(1, len(Sample.objects.all()))

    def test_2_json(self):
        Sample.objects.create(timestamp=datetime.datetime.now(tz=pytz.UTC), value=1)

        print(serializers.serialize('json', Sample.objects.all()))

    def test_3_delete(self):
        Sample.objects.all().delete()

        self.assertEqual(0, len(Sample.objects.all()))
