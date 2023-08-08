from django.db import models

# Create your models here.
class Trail(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    distance=models.IntegerField()

      # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
#   something goes down here later as well