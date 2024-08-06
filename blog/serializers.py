from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('ism', 'familiya', 'phone', 'phone_2', 'kurs', 'target')

    def to_representation(self, instance):
        return {
            'message': 'Ro`yxatdan muvofiqiyatli o`tildi'
        }
