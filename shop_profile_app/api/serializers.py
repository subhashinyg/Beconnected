from shop_profile_app.models import Shop_profile
from rest_framework import serializers
from user_app.api.serializers import AccountRegistrationSerializer



class shopSerializer(serializers.ModelSerializer):
    
    user = AccountRegistrationSerializer
    class Meta:
        model = Shop_profile
        fields = "__all__"
        