from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


# получение датчиков
# GET {{baseUrl}}/sensors/
# создание датчика
# POST {{baseUrl}}/sensors/
class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# получение информации по датчику
# GET {{baseUrl}}/sensors/1/
# обновление датчика
# PATCH {{baseUrl}}/sensors/1/
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# добавление измерения
# POST {{baseUrl}}/measurements/
class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer
