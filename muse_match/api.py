import graphene
from profiles.apis import authenticated


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Subscription(authenticated.Subscription, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, subscription=Subscription)
