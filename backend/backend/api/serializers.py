from rest_framework import serializers
from .models import Flows, Users
from rest_framework.authtoken.models import Token


class FlowSerializer(serializers.ModelSerializer):
    #anotehr way to get property
    # created_at = serializers.DateTimeField(
    #     format="%Y-%m-%H:%M", read_only=True)
    # updated_at = serializers.DateTimeField(
    #     format="%Y-%m-%H:%M", read_only=True)
    class Meta:
        model = Flows
        fields = (
            'id',
            'user_id',
            'flow_title',
            'flow_overview', 
            'flow_content',
            'created_at',
            'updated_at'
        )
        ##to get the nested data
        #depth = 1
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password','created_at','updated_at')
        # passwordはGETでアクセス禁止で必須。
        #extra_kwargs = {'password': {'write_only': True, 'required': True}}
        
    def create(self, validated_data):
        # passwordのハッシュ化
        user = Users.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user