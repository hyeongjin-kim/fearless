from django.db import models

# Create your models here.
class Champions(models.Model):
    champion_name = models.CharField(max_length=100)
    champion_image = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.champion_name