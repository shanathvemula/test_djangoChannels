import json

from app.serializers import Post, PostSerializer

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.permissions import AllowAny
from asgiref.sync import sync_to_async


# @sync_to_async
def get_posts():
    return PostSerializer(Post.objects.all(), many=True).data


class PostConsumer(GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]

    @model_observer(Post)
    async def model_changed(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_changed.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict({'data': PostSerializer(instance=instance).data, 'action': action.value})
        # return dict({'data': get_posts(), 'action': action.value})

    async def connect(self, **kwargs):
        await self.model_changed.subscribe()
        await super(PostConsumer, self).connect()
