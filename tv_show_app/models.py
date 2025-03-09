from django.db import models

class blogmanager(models.Manager):
    def validate(self,data):
        errors ={}
        if len(data['title']) < 5 or len(data['title']) > 255:
            errors['title'] = 'The title should be between 5 and 255 characters'
        if len(data['network'])< 5 or len(data['network']) > 45:
            errors['network'] = 'The network should be between 5 and 45 characters'
        if not data['desc']:
            errors['desc'] = 'You should fill the description filed'
        if  data['date'] > '10-03-2025' or data['date'] < '01-01-1950 ':
            errors['date'] = 'The release date should be between 1950 and 10-03-2025 ! '
        return errors

class tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    desc = models.TextField()
    release_date = models.DateTimeField(null='null')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = blogmanager()

# Create your models here.
