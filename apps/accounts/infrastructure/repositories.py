from apps.accounts.domain.models import CustomUser as User


class UserRepository:
    @staticmethod
    def save(user_data):
        user = User.objects.create(**user_data)
        return user