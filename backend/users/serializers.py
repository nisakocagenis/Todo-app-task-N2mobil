from rest_framework import serializers
from users.models import  User,Company,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "city")


class UserSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(source='company.name')
    class Meta:
        model = User
        fields = "__all__"



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]

