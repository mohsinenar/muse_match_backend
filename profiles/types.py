import graphene
from graphene_django.types import DjangoObjectType
from profiles import models


class UserProfileType(DjangoObjectType):
    class Meta:
        model = models.UserProfile


class MatchType(DjangoObjectType):
    profile = graphene.Field(UserProfileType)

    class Meta:
        model = models.Match
        fields = ("id", "created_at")

    def resolve_profile(self, info):
        return self.matched_user
