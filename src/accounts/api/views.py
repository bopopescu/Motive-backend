from django.contrib.auth import get_user_model

from rest_framework import authentication

from rest_framework.filters import (
		SearchFilter,
	)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from events.models import Event
from .serializers import UserCreateSerializer, UserLoginSerializer, UserDetailSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()



class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer_class = UserLoginSerializer(data=data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPIView(RetrieveAPIView):
	
	authentication_classes = (authentication.TokenAuthentication,)
	serializer_class = UserDetailSerializer

	def get(self, request, format=None):
		# if request.user:
		return Response(UserDetailSerializer(request.user).data)
		# return response(serializer.errors, status=HTTP_401_UNAUTHORIZED)



