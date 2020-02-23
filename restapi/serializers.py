from rest_framework import serializers
from bankapp.models import Indianbank

class IndianbankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indianbank
        #fields = ['bank_id','city','bank_name']
        fields = '__all__'
    