from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Profile
from board.models import Board, Comment
from board.permissions import CustomReadOnly
from board.serializer import BoardSerializer, BoardCreateSerializer, CommentSerializer, CommentCreateSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['board_type']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return BoardSerializer
        return BoardCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        print(self.request)
        serializer.save(author=self.request.user, profile=profile)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user in board.likes.all():
        board.likes.remove(request.user)
    else:
        board.likes.add(request.user)

    return Response({"status": 'ok'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return CommentSerializer
        return CommentCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)