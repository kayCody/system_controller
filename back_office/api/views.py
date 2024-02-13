from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from database.models import Member
from .serializer import MemberSerializer
import random


# Create your views here.

# GNACOFA MEMBER FORM API ROUTE///
'''
class MemberView(generics.CreateAPIView):
  querset = Member.objects.all()
  serializer_class = MemberSerializer


class GenerateCodeView(View):
    def get(self, request):
        # Generate a random 6-digit code
        random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Create a VerificationCode object and save it to the database
        verification_code = VerificationCode(code=random_code)
        verification_code.save()

        return render(request, 'your_template.html', {'code': random_code})

@api_view(['GET', 'POST'])
def GenerateToken(request):
  random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)]) # Generate a random 6-digit code
  # Create a VerificationCode object and save it to the database
  generated_code = Token(token=random_code)
  generated_code.save()
  return render(request, {'code': random_code})

@api_view(['GET', 'POST'])
def AuthenticateToken(request):
  pass
'''

# members Registrationn form
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
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

