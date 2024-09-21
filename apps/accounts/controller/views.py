from apps.accounts.application.use_cases import RegisterUserUseCase
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UserRegistrationViewSet(ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            # Executa o caso de uso
            user = RegisterUserUseCase.execute(user_data)
            return Response({"message": "User registered successfully", "user": user}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
