from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination
from .models import User
from .serializers import UserSerializer


class UserList(APIView):

    def get(self, request, format=None):
        name = request.query_params.get('name')
        sort = request.query_params.get('sort', 'id')  # Default sort by 'id'

        queryset = User.objects.all()
        if name:
            queryset = queryset.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if sort:
            descending = '-' in sort
            sort_field = sort.replace('-', '')
            queryset = queryset.order_by(f'-{sort_field}' if descending else sort_field)

        # Implementing pagination
        paginator = pagination.PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 5)
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        print("user",user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
