from django.db import models

# Create your models here.

# After loking at the wireframe create 
# the class/classes you would need and 
# any relationships necessary then..

# Write out in a different file:

# 1.) How would you get all Yasmin's tasks, 
#    assuming you know her ID is 3?
# 2.) How would you create a new task with Yasmin as the owner?
# 3.) How would you print the owner's name of Task  with ID 23?

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # probably other fields here
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tasks

class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    # maybe other fields
    owner = models.ForeignKey(User, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
