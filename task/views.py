from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from register.serializers import UserSerializer
from .models import Task
from .serializers import SerializerTask
from rest_framework.pagination import PageNumberPagination
#from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .filters import TaskFilter

# Create your views here.
#Create profile
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user)
    serializer = UserSerializer(instance = request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Create Task list

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createTask(request):
    serializer = SerializerTask(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message":"Tarea creada",
                        "serializer":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Update List
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateTask(request,task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    serializer = SerializerTask(instance=task, data= request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"estatus:":"Tarea actualizada",
                        "data:":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Get List
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskList(request):
    task_list = Task.objects.filter(user= request.user)

    paginator = PageNumberPagination()
    paginator.page_size = request.query_params.get('limit',10)
    resutl_page = paginator.paginate_queryset(task_list, request)

    serializer = SerializerTask(resutl_page, many=True)
    return paginator.get_paginated_response({
        'data': serializer.data,
        'page': paginator.page.number,
        'limit': paginator.page_size,
        'total': paginator.page.paginator.count,
    })

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTask(request,task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = SerializerTask
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = {'title':['contains'],
                        'completed': ['exact']}


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]