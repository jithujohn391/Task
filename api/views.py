from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# accounts/views.py

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
# @api_view(['GET'])
# def view_user(request):
	
	
# 	# checking for the parameters from the URL
# 	if request.query_params:
# 		users = User.objects.filter(**request.query_params.dict())
# 	else:
# 		users = User.objects.all()

# 	# if there is something in items else raise error
# 	if users:
# 		serializer = UserSerializer(users, many=True)
# 		return Response(serializer.data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
	
# @api_view(['POST'])
# def update_user(request, pk):
# 	user = User.objects.get(pk=pk)
# 	data = UserSerializer(instance=user, data=request.data)

# 	if data.is_valid():
# 		data.save()
# 		return Response(data.data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
	
# @api_view(['DELETE'])
# def delete_user(request, pk):
# 	user = get_object_or_404(User, pk=pk)
# 	user.delete()
# 	return Response(status=status.HTTP_202_ACCEPTED)




