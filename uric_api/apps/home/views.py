from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("HOME")

from rest_framework.views import APIView
from rest_framework.response import Response
class TestAPIView(APIView):
    def get(self,request):
        from django.db import DatabaseError
        raise DatabaseError("mysql连接失败")
        return Response({"message": "hello"})