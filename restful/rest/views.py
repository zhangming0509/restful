from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest.models import RequestInfo
from rest.serializers import RequestInfoSerializer

from rest_framework import viewsets
from rest.serializers import HyperRequestInfoSerializer
    
class RequestInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RequestInfo.objects.all()
    serializer_class = HyperRequestInfoSerializer


@api_view(['GET', 'POST'])
def request_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        requestinfos = RequestInfo.objects.all()
        serializer = RequestInfoSerializer(requestinfos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RequestInfoSerializer(data=request.DATA)
        if serializer.is_valid():
            try:
                serializer.send_to_dedicated()
                serializer.send_to_requester()
            except:
                pass
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        requestinfo = RequestInfo.objects.get(pk=pk)
    except RequestInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RequestInfoSerializer(requestinfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RequestInfoSerializer(requestinfo, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        requestinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
