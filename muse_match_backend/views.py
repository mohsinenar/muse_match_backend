from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    return render(request, 'home.html')
