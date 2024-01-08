from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration, Banner
from rest_framework import status


class RegistrationListCreateAPIView(APIView):

    def post(self, request):
        data = request.data
        ism = data.get('ism')
        familiya = data.get('familiya')
        phone = data.get('phone')
        kurs = data.get('kurs')
        note = data.get('note')
        if ism and familiya and phone and kurs:
            Registration.objects.create(ism=ism, familiya=familiya, phone=phone, kurs=kurs, note=note)
            return Response({'message': 'Ro`yxatdan muvofiqiyatli o`tildi'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Ma`lumot to`liq emas'}, status=status.HTTP_400_BAD_REQUEST)


class BannerListCreateAPIView(APIView):
    def get(self, request):
        banner = Banner.objects.values("title", "description").first()
        return Response({
            "status": "ok",
            "data": banner
        })
    