from django.db import models

# Models Written and this will be stored in the database table and later retrieved using Project class
# object in the home.html file
# We can also add same Project rows direcly from the django admin
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    # This function will help us to return the same name of the project as defined by us while creating in django admin
    def __str__(self):
        return self.title
