from django.db import models

# Create your models here.

class apiBox(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stats = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
<<<<<<< HEAD
=======

class Project(models.Model):
    name = models.CharField(max_length=255)
    # user_id = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    token = models.UUIDField()

    def __str__(self):
        return self.name
>>>>>>> 4089fc8986c5b3fd5deef63645f8ad3f04b2b6ee
