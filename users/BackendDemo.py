from django.contrib.auth.hashers import check_password
from .models import GrouperUser


class MyBackend(object):
    def authenticate(self, username=None, password=None):
        login_valid = ('admin1' == username)
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        pwd_valid = (password == '123123')
        print(username, password, "---in backend")
        if login_valid and pwd_valid:
            try:
                user = GrouperUser.objects.get(username=username)
            except GrouperUser.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = GrouperUser(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return GrouperUser.objects.get(pk=user_id)
        except GrouperUser.DoesNotExist:
            return None