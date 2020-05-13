"""
store models
"""
from django.db import models
from django.utils.text import slugify
from authentication.models import User


class Store(models.Model):
    """
    store class
    """
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="images/covers", blank=True)


    def get_absolute_url(self):
        """
        function to get absolute url of store
        """
        return f"/store/{self.slug}"
    
    def save(self, *args, **kwargs):
        """
        overiding save method
        """
        self.slug = slugify(self.name)
        super(Store, self).save(*args, **kwargs)

    
    def __str__(self):
        """
        string representation of store
        """
        return self.name
