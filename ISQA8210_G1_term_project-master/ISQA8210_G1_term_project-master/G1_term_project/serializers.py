# import serializer from rest_framework
from .models import Listing
from rest_framework import serializers


# create a serializer
class ListingSerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Listing
        fields = '__all__'