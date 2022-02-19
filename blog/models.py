from django.db import models
from django.template.defaultfilters import slugify
from user_auth.models import Account
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name} '

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super(Blog, self).save(*args, **kwargs)

