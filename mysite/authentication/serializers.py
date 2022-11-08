
from authentication.models import User
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.validators import RegexValidator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)


    class Meta:
        model = User
        fields = ['id', 'username',  'full_name', 
                  'birth_date', 'age', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class LoginSerializer(serializers.Serializer):
    tokens = serializers.SerializerMethodField()
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},  write_only=True)

    def get_tokens(self, obj):
        return {
            'refresh': obj.tokens()['refresh'],
            'access': obj.tokens()['access']
        }

    class Meta:
        fields = ['id', 'username', 'password', 'tokens']


    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        self.error_messages['no_active_account'] = _(
            'Account disabled, contact admin'
        )

        user = auth.authenticate(
            username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed(
                self.error_messages['no_active_account'], code='no_active_account')

        # TODO: uncomment after doing the phone verification
        # if not user.phone_verified:
        #     raise AuthenticationFailed('Phone is not verified')

        return user
        



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
