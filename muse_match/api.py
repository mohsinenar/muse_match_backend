import graphene

from profiles.apis import authenticated


class Query(authenticated.Query):
    pass


class Subscription(authenticated.Subscription, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, subscription=Subscription)
