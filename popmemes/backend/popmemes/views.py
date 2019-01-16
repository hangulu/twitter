from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemeSerializer
from .models import Popmemes

import find_memes as fm

# Create your views here.
class MemeView(viewsets.ModelViewSet):
    serializer_class = MemeSerializer
    lookup_field = 'user'
    queryset = Popmemes.objects.all()

    @api_view(['POST', 'GET'])
    def show_popmeme(request):
        """
        Show the most popular meme on the timeline.
        """
        # When the user hits submit
        if request.method == 'POST':
            username = request.data
            image, freq = fm.memr(username)
            # image, freq = "meme1", 25.
            # Serialize the response, check its validity, then save
            serializer = MemeSerializer({'user': username, 'pop_img': image, 'freq': freq})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            # Get the meme by the username
            try:
                meme = Popmemes.objects.get(user=request.data)
            except ValueError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            # Serialize the meme then return it
            serializer = MemeSerializer(meme)
            return Response(serializer.data)
