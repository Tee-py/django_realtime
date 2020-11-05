from django.shortcuts import render, redirect
from .models import *
import secrets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Notification

# Create your views here.

def home(request):
    return render(request, "home.html")


@api_view(["GET"])
@permission_classes([])
def get_notifications(request):
    return Response({
        "status": True,
        "data": NotificationSerializer(Notification.objects.all(), many=True).data
    })