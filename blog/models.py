from django.db import models

# This model will be wrtten in database as Table, if any changes are made in this class, we need to run belo commands
# python manage.py makemigrations &
# python manage.py migrate
# If we add any function to this class we don't need to migrate
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    date = models.DateField()

    def __str__(self):
        return self.title
