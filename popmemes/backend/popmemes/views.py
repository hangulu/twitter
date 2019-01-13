from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemeSerializer
from .models import Popmemes

# import popmemes.main as pm

# Create your views here.
class MemeView(viewsets.ModelViewSet):
    serializer_class = MemeSerializer
    queryset = Popmemes.objects.all()

    @api_view(['POST', 'GET'])
    def show_popmeme(request):
        """
        Show the most popular meme on the timeline.
        """
        # When the user hits submit
        if request.method == 'POST':
            username = request.data
            # image, freq = pm.memr(username)
            image, freq = "meme1", 25.
            return Response({'pop_image': image, 'frequency': freq}, status=status.HTTP_201_CREATED)
