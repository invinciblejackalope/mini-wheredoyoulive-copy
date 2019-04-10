from django.db import models

# https://docs.djangoproject.com/en/2.1/topics/db/models/
# https://stackoverflow.com/questions/2257635/django-unique-field-generation


# User model: contains properties
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    # what to return if str() is called on a user, used for debugging/testing
    def __str__(self):
        return self.values()
