from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemeSerializer
from .models import PopImage

import popmemes.find_memes as fm

@api_view(['POST', 'GET'])
def show_popimg(request):
    """
    Show the most popular meme on the timeline.

    request (HTTP request): Data submitted via the form.
    return: data with HTTP response
    """
    # When the user hits submit
    if request.method == 'POST':
        username = (request.body).decode('utf-8')
        # image, freq = fm.memr(username)
        image, freq = "meme2", 5.
        # Serialize the response, check its validity, then save
        serializer = MemeSerializer(data={'user': username, 'pop_img': image, 'freq': freq})
        if serializer.is_valid():
            # Save the serialized data in the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        # Get all memes
        try:
            memes = PopImage.objects.all()
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Serialize the meme then return it
        serializer = MemeSerializer(memes, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def popimg_detail(request, user):
    """
    Retrieve, update or delete a user by their username.

    request (HTTP request): Data submitted via the form.
    user (string): The username to be examined.
    return: data with HTTP response
    """
    try:
        meme = PopImage.objects.filter(user=user).first()
    except ValueError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Get the information on this user
        serializer = MemeSerializer(meme, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update this user
        serializer = MemeSerializer(meme, data=request.data, context={'request': request})
        if serializer.is_valid():
            # Save to the database
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete this user
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
