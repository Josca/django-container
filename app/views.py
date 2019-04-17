import http

from django.http import HttpResponse
from django.shortcuts import render

from prometheus_client import Counter

from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema
import coreapi


class Writer(APIView):
    # description for Swagger
    schema = AutoSchema(manual_fields=[
        coreapi.Field("value", required=False, location='query', description='writen value', example=''),
        coreapi.Field("desc", required=False, location='query', description='writen value description', example=''),
    ])

    QUERY_PARAMS = ['value', 'desc']
    prometheus_counter = Counter('writer_counter', 'written data counter', labelnames=QUERY_PARAMS)

    def get(self, request):
        """
        Example writen to swagger?
        """

        label_vals = dict()
        for label in self.QUERY_PARAMS:
            val = request.GET.get(label, None)
            if val is None:
                return HttpResponse(status=http.HTTPStatus.BAD_REQUEST, content='label "%s" is missed' % label)
            label_vals[label] = val

        self.prometheus_counter.labels(**label_vals).inc()
        return HttpResponse(status=http.HTTPStatus.OK, content="OK")


class Health(APIView):

    def get(self, _request):
        """
        check if server is running
        """

        return HttpResponse(status=http.HTTPStatus.OK, content="OK")


def index(request):
    return render(request, 'index.html')
