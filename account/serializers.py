from rest_framework import serializers
from account.models import MyUser
from account.utils import send_activation_code
#TODO: login serializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        print(validated_data)
        password = validated_data.get('password')
        password_confirm = validated_data('password_confirm')
#TODO: спросить что значит очищенные данные? от чего очищает validate, что за проверка
#TODO: и что-то про пароли, почему мы указываем их тут,разве это не тоже
#TODO: самое, если передать в моделях?
        if password_confirm != password_confirm:
            raise serializers.ValidationError("Passwords don't match")
        return validated_data

    def create(self, validated_data):
        """This function is called when self.save() method is called"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user







