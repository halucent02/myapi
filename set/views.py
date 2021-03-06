from django.shortcuts import render
from .serializers import SetSerializer
from .models import Set
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class SetListCreateView(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)
    serializer_class       = SetSerializer
    permission_classes     = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = SetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self, format=None):
        sort     = self.request.query_params.get('sort', None)
        limit    = self.request.query_params.get('limit', None)
        queryset = Set.objects.all()

        if limit and sort:
            queryset = queryset.all().order_by(sort)[:int(limit)]
        if limit and not sort:
            queryset = queryset.all()[:int(limit)]
        if not limit and sort:
            queryset = queryset.all().order_by(sort)
        return queryset

class SetRetrieveView(RetrieveAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)
    serializer_class       = SetSerializer
    permission_classes     = (IsAuthenticated,)
    queryset               = Set.objects.all()