from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Building
from .serializers import ContactFormSerializer, JoinUsFormSerializer, BuildingSerializer, ContractRequestFormSerializer
from accounts.models import User


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
    filterset_fields = ['building_type', 'building_age', 'building_area', 'key_place', 'building_category', 'building_usage','offer','price','soom_price','payment_method','rooms','floors','baths','apartments','ground_floor_rooms','upper_floor_rooms','split_air_conditioner','window_air_conditioner','hall','parking','extension','driver_room','elevators','kitchen','seperated_entrance','warehouse','car_entrance','shared_entrance','seperated_2_floors','Central_air_conditioning','gas','sauna','pool','electricity','rooftop','mez_hall','well','pieces','piece_number','design_number','region','city','neighborhood','latitude','longitude']


class GetEstateView(APIView):
    def get(self, request, pk):
        estate = Building.objects.get(pk=pk)
        serializer = BuildingSerializer(estate)
        return Response(serializer.data, status=status.HTTP_200_OK)
