from graphene_django.types import DjangoObjectType
from profiles import models


class UserProfileType(DjangoObjectType):
    class Meta:
        model = models.UserProfile
