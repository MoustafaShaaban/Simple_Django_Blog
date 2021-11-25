from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        """ Show new posts first  """
        ordering = ['-updated_on']


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """ A method to tell Django how to calculate the canonical URL (official url of a page) for an object """
        return reverse('post-detail', kwargs={'slug': self.slug})
