from dataclasses import fields
from pyexpat import model
from user_app.models import Account
from rest_framework import serializers




class AccountRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = Account
        fields = ['full_name', 'email', 'password', 'password2','phone']
        extra_kwargs = {
            'password':{'write_only':True}
        }

 

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2 :
            raise serializers.ValidationError({'error':'Password should be the same'})

        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email id already exists'})

        if Account.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error':'phone number already exists'})    
        
        account = Account(
            full_name=self.validated_data['full_name'],
            email = self.validated_data['email'],
            phone= self.validated_data['phone'],
            )
        account.set_password(password)
        account.save()

        return account

class UserProfileAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','phone']
