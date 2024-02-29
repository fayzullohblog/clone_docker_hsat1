from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username,phone_number, first_name=None, last_name=None, password=None,):
        if not username:
            raise ValueError("User must have a phone number")
        if not password:
            raise ValueError("User must have a Password")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, username,phone_number,first_name=None, last_name=None, password=None):
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,

        )

        user.is_superuser=True
        # user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_boss=True
        user.save(using=self._db)
        return user