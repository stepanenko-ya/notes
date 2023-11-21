from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        serializer_data = UserSerializer(user).data
        return Response({
            'user': serializer_data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            serializer_data = UserSerializer(user).data
            return Response({
                'user': serializer_data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            RefreshToken(request.data.get('refresh_token')).blacklist()
            return Response({'detail': 'Successfully logged out.'},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Error during logout.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
