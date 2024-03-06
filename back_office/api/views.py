from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from database.models import Member
from .serializer import MemberSerializer
import random


# Applicants portal
@api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
def MembershipView(request, format=None):
  if request.method == 'GET':
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

