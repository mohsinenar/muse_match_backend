from profiles import models


def create_pofile(backend, user, response, is_new=False, *args, **kwargs):
    models.UserProfile.objects.get_or_create(user=user, gender="M", looking_for="F")
