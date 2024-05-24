from rest_framework.routers import DefaultRouter
from django.urls import path
from app.views import PostView  # , index

# router = DefaultRouter()
#
# router.register("post", PostViewSet, basename='post')

urlpatterns = [
    # path("", view=index),
    path('post', PostView.as_view())
]

# urlpatterns += router.urls
