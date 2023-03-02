import graphene
from graphene_subscriptions.events import CREATED

from profiles import models
from profiles import types


def get_user_from_context(info):
    return models.UserProfile.objects.get(user=info.context.user)


class Query(graphene.ObjectType):
    my_profile = graphene.Field(types.UserProfileType)

    def resolve_my_profile(self, info, **kwargs):
        return get_user_from_context(info)


class DeleteProfileImageMutation(graphene.Mutation):
    class Arguments:
        ids = graphene.List(graphene.Int, required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, ids: list[int]):
        profile = get_user_from_context(info)
        profile.images.filter(id__in=ids).delete()
        return DeleteProfileImageMutation(success=True)


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
        profile = get_user_from_context(info)
        profile.name = name
        profile.save()
        return UpdateMyProfileMutation(profile=profile)


class Subscription(graphene.ObjectType):
    my_matches = graphene.String()

    def resolve_my_matches(root, info):
        return ""


class Mutation(graphene.ObjectType):
    delete_user_image = DeleteProfileImageMutation.Field(description="Delete user mutation")
