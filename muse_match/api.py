import graphene
from rx import Observable


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    def resolve_hello(self, info):
        return info.context.user


import graphene
from rx import Observable
from profiles import types, models
from graphene_subscriptions.events import CREATED


class Subscription(graphene.ObjectType):
    hello = graphene.String()
    user_profile_created = graphene.Field(types.UserProfileType)

    def resolve_hello(root, info):
        return Observable.interval(1000) \
            .map(lambda i: type())

    def resolve_user_profile_created(root, info):
        return root.filter(
            lambda event:
            event.operation == CREATED and
            isinstance(event.instance, models.UserProfile)
        ).map(lambda event: event.instance)


schema = graphene.Schema(query=Query, subscription=Subscription)
