from django.contrib.auth import authenticate
from KasuwanDauriInventory.helpers import renderResponse
from UserServices.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SignupAPIView(APIView):
    def post(self, request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        profile_pic=request.data.get('profile_pic')

        emailCheck=Users.objects.filter(email=email)
        if emailCheck.exists():
            return renderResponse(data='Email already exists', message='Email Already exist' , status=status.HTTP_400_BAD_REQUEST)
        
        usernameCheck=Users.objects.filter(username=username)
        if usernameCheck.exists():
            return renderResponse(data='Username already exists', message='Username Already exist', status=status.HTTP_400_BAD_REQUEST)

        if username is None or email is None or password is None:
            return renderResponse(data='Please provide username, email and password', message='Please provide username, email and password', status=status.HTTP_400_BAD_REQUEST)
        user=Users.objects.create_user(username=username,email=email,password=password,profile_pic=profile_pic)
        if request.data.get('domain_user_id'):
            user.domain_user_id=Users.objects.get(id=request.data.get('domain_user_id'))
        user.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        access['username'] = user.username
        access['email'] = user.email
        access['profile_pic'] = user.profile_pic
        


        return Response({'access': str(access), 'refresh': str(refresh),'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return renderResponse(data='Please provide both username and password', message='Please provide both username and password', status=status.HTTP_400_BAD_REQUEST)


        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            access['profile_pic'] = user.profile_pic

            return Response({
                'refresh': str(refresh),
                'access': str(access),
            })
        else:
            return renderResponse(data='Invalid credentials', message='Invalid credentials', status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        return renderResponse(data='Please use POST method to login', message='Please use POST method to login', status=status.HTTP_400_BAD_REQUEST)

    


class PublicAPIView(APIView):
    def get(self, request):
        return renderResponse(data='This is a public API', message='This is a public API', status=status.HTTP_400_BAD_REQUEST)


class ProtectedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return renderResponse(data='This is a protected API', message='This is a protected API', status=status.HTTP_400_BAD_REQUEST)
