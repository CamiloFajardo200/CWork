from django.contrib.auth.models import User, Group
from blog.models import Post
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


schema_view = get_swagger_view(title=' API')

urlpatterns = [
    url(r'^$', schema_view)
]