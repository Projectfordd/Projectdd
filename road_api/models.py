from django.db import models

class Road(models.Model):
    name = models.CharField(max_length=255)
    temp = models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name