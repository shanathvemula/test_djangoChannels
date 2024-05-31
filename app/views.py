from django.http import HttpResponse
from django.contrib.auth.models import User
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
            data['author'] = User.objects.get(username__exact=data['author']).id
            serializer = PostSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            data = request.data
            post = Post.objects.get(id=data['id'])
            if 'author' in data.keys():
                data['author'] = User.objects.get(username__exact=data['author']).id
            serializer = PostSerializers(post, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            data = request.data
            post = Post.objects.get(id=data['id'])
            if post.delete()[0]:
                return HttpResponse(JSONRenderer().render({"Message": "Deleted Successfully"}), content_type='application/json',
                                    status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)
