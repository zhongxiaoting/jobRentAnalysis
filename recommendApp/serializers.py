from rest_framework import serializers
from recommendApp.models import Job, Renting


class JobSerializer(serializers.ModelSerializer):
    """
    测试前提交的信息
    """

    class Meta:
        model = Job
        fields = "__all__"


class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = "__all__"
