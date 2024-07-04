# Create your views here.
from rest_framework import generics
from .models import User, Quote
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .rabbitmq import send_message
from rest_framework import status
import random
import hashlib
import json
from django.shortcuts import get_object_or_404, render

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class QuoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data        

        if not data:
            return Response({"error": "Vehicle type and value are required"}, status=status.HTTP_400_BAD_REQUEST)
   
        # generate an id of quote
        quote_id= hashlib.md5(json.dumps(data).encode("utf-8")).hexdigest()
        
        messagejson = {}
        messagejson['quote_id'] = quote_id
        messagejson['quote_body'] = data
        json_data = json.dumps(messagejson)
       
        print(" [x] Tryind Sent %r" % json_data)
        send_message(json_data)        
        return Response({"quote_id": quote_id})
