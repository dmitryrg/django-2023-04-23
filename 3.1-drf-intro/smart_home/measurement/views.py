# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.prefetch_related('measurements').all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        return Response({'status': 'OK'})

    def putch(self, request):
        return Response({'status': 'OK'})

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.prefetch_related('measurements').all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        return Response({'status': 'OK'})

    def putch(self, request):
        return Response({'status': 'OK'})
class MeasurementView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
