from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .permissions import AllowAny




class RegisterApiView (APIView) : 
    def get (self , request) : 
        return Response (
            {"messages": "error please sir again!!!"} ,
              status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

    def post (self , request) : 
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password : 
            return Response ({"messages": "invalid password or username!!!"},status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username = username).exists() : 
            return Response ({"messages" : "this user is exits!!!"} , status=status.HTTP_400_BAD_REQUEST)
        
        else : 
            User.objects.create_user(username= username ,password= password)
            return Response ({"messages" : "done successfully!!!"} , status=status.HTTP_201_CREATED)




class LoginApiView(APIView) : 
    permission_classes = [AllowAny]
    authentication_classes = []
    def get (self , request) : 
        return Response ({"message" : "sir input is get please again!!!"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post (self , request) : 
        username = request.data.get("username") 
        password = request.data.get("password")

        if not username or not password : 
            return Response ({"message" : "username or password required!!!"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username , password=password)
        if user is None : 
            return Response ({"messages" : "invalid user please again!!!"} , status=status.HTTP_401_UNAUTHORIZED)
        
        else : login(request ,user)
        return Response ({"messages" : "ok sir login successfully"} , status=status.HTTP_200_OK)
    



class LogoutApiView (APIView) : 
    def post (self , request) : 
        logout(request)
        return Response ({"message" : "logout successfuly"} , status=status.HTTP_200_OK)