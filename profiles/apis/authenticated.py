import graphene
from graphene_subscriptions.events import CREATED
from rx import Observable

from profiles import types, models


class Subscription(graphene.ObjectType):
    my_matches = graphene.Field(types.MatchType)

    def resolve_my_matches(root, info):
        return root.filter(
            lambda event:
            event.operation == CREATED and
            isinstance(event.instance, models.Match)
        ).map(lambda event: event.instance)
