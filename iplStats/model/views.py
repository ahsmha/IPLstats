from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import TeamSerializer
from .models import Team


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_teams(request):
    data = Team.objects.all()
    serializer = TeamSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer