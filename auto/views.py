from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny

from auto.models import Auto
from auto.serializers import (
    AutoCreateSerializers,
    AutoSerializers,
    AutoUpdateSerializer,
)


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        if request.user.role == 'admin':
            return True
        return False


class AutoCreateView(generics.CreateAPIView):
    serializer_class = AutoCreateSerializers
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AutoSerializers
    queryset = Auto.objects.all()


class AutoUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsUser]
    serializer_class = AutoUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
    queryset = Auto.objects.all()


class AutoDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsUser]
    queryset = Auto.objects.all()