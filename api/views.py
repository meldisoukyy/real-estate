from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Building
from .serializers import ContactFormSerializer, JoinUsFormSerializer, BuildingSerializer, ContractRequestFormSerializer


class EstateFilter(django_filters.FilterSet):
    building_type = django_filters.CharFilter(field_name='building_type', lookup_expr='icontains')
    building_category = django_filters.CharFilter(field_name='building_category', lookup_expr='icontains')

    class Meta:
        model = Building
        fields = ['building_type', 'building_age', 'building_area', 'key_place', 'building_category', 'building_usage']


# Create your views here.
class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class ContractRequestFormView(APIView):
    def post(self, request):
        serializer = ContractRequestFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class JoinUsFormView(APIView):
    def post(self, request):
        serializer = JoinUsFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class AddEstateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BuildingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class GetAllEstatesView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'building_type':['exact'],
                        'building_age':['exact'],
                        'building_area':['exact'],
                        'key_place':['exact'],
                        'building_category':['exact'],
                        'building_usage':['exact'],
                        'offer':['exact'],
                        'price': ['lte', 'gte'],
                        'soom_price': ['lte', 'gte'],
                        'payment_method':['exact'],
                        'rooms':['exact'],
                        'floors':['exact'],
                        'baths':['exact'],
                        'apartments':['exact'],
                        'ground_floor_rooms':['exact'],
                        'upper_floor_rooms':['exact'],
                        'split_air_conditioner':['exact'],
                        'window_air_conditioner':['exact'],
                        'hall':['exact'],
                        'parking':['exact'],
                        'extension':['exact'],
                        'driver_room':['exact'],
                        'elevators':['exact'],
                        'kitchen':['exact'],
                        'seperated_entrance':['exact'],
                        'warehouse':['exact'],
                        'car_entrance':['exact'],
                        'shared_entrance':['exact'],
                        'seperated_2_floors':['exact'],
                        'Central_air_conditioning':['exact'],
                        'gas':['exact'],
                        'sauna':['exact'],
                        'pool':['exact'],
                        'electricity':['exact'],
                        'rooftop':['exact'],
                        'mez_hall':['exact'],
                        'well':['exact'],
                        'pieces':['exact'],
                        'piece_number':['exact'],
                        'design_number':['exact'],
                        'region':['exact'],
                        'city':['exact'],
                        'neighborhood':['exact'],
                        'latitude':['exact'],
                        'longitude':['exact']}


class GetEstateView(APIView):
    def get(self, request, pk):
        estate = Building.objects.get(pk=pk)
        serializer = BuildingSerializer(estate)
        return Response(serializer.data, status=status.HTTP_200_OK)
