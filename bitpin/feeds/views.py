from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import FeedSerializer, UserRateSerializer
from .models import Feed, UserRate
from rest_framework.response import Response
from rest_framework import status


class FeedView(ReadOnlyModelViewSet):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()


class UserRateView(ModelViewSet):
    serializer_class = UserRateSerializer
    queryset = UserRate.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

