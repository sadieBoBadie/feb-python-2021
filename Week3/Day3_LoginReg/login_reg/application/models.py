from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}

        # logic here
        # Check len of inputs / blank?
        # email -- pattern validation (regex)
        if not EMAIL_REGEX.matchcopy(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        # check if email in DB already
        user = User.objects.filter(email = postData["email"])
        # if not there will return []
        # if it is there --> [<User Object at 0xbsdlfkjsdflkj>]
        # password -- 
        if user:
            errors['user'] = "Account already exists."
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()