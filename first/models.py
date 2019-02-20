from django.db import models

class Document(models.Model):
    slug = models.SlugField()
    file = models.FileField(upload_to='object')

    def __str__(self):
        return self.slug

class Programming(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField()
    value=models.TextField()

    def __str__(self):
        return self.slug
