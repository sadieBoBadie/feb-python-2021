from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    
    def basic_validator(self, postData):
         # create a dictionary of messages 
        errors = {}

        if len(postData["title"]) == 0:
            errors["title"] = "Title must not be blank."

        if len(postData["network"]) == 0:
            errors["network"] = "Network must not be blank."

        if len(postData["description"]) == 0:
            errors["description"] = "Description must not be blank."

        if len(postData["release_date"]) == 0:
            errors["release_date"] = "Release date required."

        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __repr__(self):
        return f"Show: {self.title} {self.network}"
    