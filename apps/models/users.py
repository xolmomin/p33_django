from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    phone = CharField(max_length=11, null=True, unique=True)

    @property
    def full_name(self):
        if len(self.get_full_name()) == 0:
            return self.username
        return self.get_full_name()
