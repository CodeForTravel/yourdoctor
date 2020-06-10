from rest_framework import serializers

from addresses.models import Country,Division,City,Area,Address



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = ("id", "name")

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ("id", "name")

# class AreaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Area
#         fields = ("id", "name")