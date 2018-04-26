from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from apk_parse.apk import APK
from backoffice.models import *
import uuid


class ApplicationsAPI(viewsets.ViewSet):
    def list(self, request):
        try:
            data = Applications.objects.all().values()
            for i in data:
                i.update({'app': Applications.objects.get(id=i['id']).app.url})
            return Response(data, status=status.HTTP_200_OK)
        except Exception as err:
            data = {'err': str(err)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        if request.FILES.get('file'):
            try:
                f = request.FILES.get('file')
                f.name = str(uuid.uuid1().hex) + '.apk'
                a = Applications()
                a.app = f
                a.save()
                apkf = APK(a.app.path)
                a.package_name = apkf.package
                a.package_version = apkf.get_androidversion_name()
                a.save()

                data = Applications.objects.filter(id=a.id).values()[0]
                data.update({'app': a.app.url})

                return Response(data, status=status.HTTP_200_OK)
            except Exception as err:
                data = {'status': 0, 'msg': str(err)}
                return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)