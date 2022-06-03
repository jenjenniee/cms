from rest_framework import serializers
from cms.models import Plan


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'