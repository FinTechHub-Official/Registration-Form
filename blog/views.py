from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration, Banner
from .serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView


class RegistrationListCreateAPIView(CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class BannerListCreateAPIView(APIView):
    def get(self, request):
        banner = Banner.objects.values("title", "description").first()
        return Response({
            "status": "ok",
            "data": banner
        })
    