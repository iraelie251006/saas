from django.db import models

# Create your models here.
class PageVisit(models.Model):
    """
    Model to store visit information.
    """
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

