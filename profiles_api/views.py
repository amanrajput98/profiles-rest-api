from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from profiles_api import serializers


class HelloApiView(APIView):
    """Test APi view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch ,put, delete)',
            'Is Similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = 'Hello {} ur age is {}'.format(name, age)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({'method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, partial updates)',
            'Automatically maps to URLs using routers',
            'Provide more functionality using less code'
        ]
        return Response({'message': 'Hello!!!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = 'Hello {} and age = {}'.format(name, age)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its Id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating the object"""
        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle the partial updates of object"""
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy or delete the object"""
        return Response({'message': 'Delete'})