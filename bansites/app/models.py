from django.db import models

# Create your models here.


class SiteModel(models.Model):

      url = models.URLField(max_length=200)
      unsafe_score = models.IntegerField(default=30)
      uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
      updated_at = models.DateTimeField(auto_now_add=True, blank= True)
