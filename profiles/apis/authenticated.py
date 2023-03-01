import graphene
from graphene_subscriptions.events import CREATED

from profiles import models
from profiles import types


class Query(graphene.ObjectType):
    my_profile = graphene.Field(types.UserProfileType)

    def resolve_my_profile(self, info, **kwargs):
        user = models.UserProfile.objects.get(user=info.context.user)
        return user


class UpdateMyProfileMutation(graphene.Mutation):
    class Arguments:
        mame = graphene.String(required=True)
        # age = graphene.Int(required=True)
        # height = graphene.Int(required=True)
        # tagline = graphene.String(required=True)
        # about_me = graphene.String(required=True)

    profile = graphene.Field(types.UserProfileType)

    @classmethod
    def mutate(cls, root, info, name):
        profile = models.UserProfile.objects.get(user=info.context.user)
        profile.name = name
        profile.save()
        return UpdateMyProfileMutation(profile=profile)


class Subscription(graphene.ObjectType):
    my_matches = graphene.Field(types.MatchType)

    def resolve_my_matches(root, info):
        return root.filter(
            lambda event:
            event.operation == CREATED and
            isinstance(event.instance, models.Match)
        ).map(lambda event: event.instance)
