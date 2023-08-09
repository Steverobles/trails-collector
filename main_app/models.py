from django.db import models
from django.urls import reverse

# Create your models here.
class Trail(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    distance=models.CharField()

      # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
#   something goes down here later as well

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  # Add this method
    def get_absolute_url(self):
     return reverse('detail', kwargs={'trail_id': self.id})