from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from app.serializers import Post, PostSerializer, PostSerializers


# Create your views here.

class PostView(APIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            client = Post.objects.all()
            serializer = PostSerializer(client, many=True)
            return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = PostSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)


# def index(request):
#     return render(request, 'index.html', context={'post': Post.objects.all()})
