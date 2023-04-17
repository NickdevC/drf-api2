from rest_framework import generics, permissions
from drf_api2.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follwer.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    No update view, as we either follow or unfollow users.
    Destroy a follower, i.e. unfollow someone if owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
