from django.urls import path
from rest_framework import routers

from board.views import BoardViewSet, like, CommentViewSet

router = routers.SimpleRouter()

router.register('board', BoardViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>', like, name='like'),

]
