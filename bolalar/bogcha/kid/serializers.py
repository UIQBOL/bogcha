from rest_framework import serializers
from .models import Staff

class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=['id', 'name', 'lastname', 'image']

