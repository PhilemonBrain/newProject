from django.db import models

#Models for all the API's in the database
class ApiList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stats = models.CharField(max_length=255, default='3hrs')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    # user_id = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    token = models.UUIDField()

    def __str__(self):
        return self.name
