from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import CharField, EmailField

from apps.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email')
        field_classes = {"username": UsernameField}
