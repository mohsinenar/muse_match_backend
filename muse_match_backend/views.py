from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    return render(request, 'home.html')


from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from muse_match_backend.api import schema


class PrivateGraphQLView(GraphQLView, LoginRequiredMixin):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, schema=schema, graphiql=True, **kwargs)
        return view
