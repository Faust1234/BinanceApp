from django.db import models

# Create your models here.
class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name
