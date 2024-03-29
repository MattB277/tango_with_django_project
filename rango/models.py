from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    MAX_NAME_LENGTH = 128
    name = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Page(models.Model):
    MAX_TITLE_LENGTH = 128
    MAX_URL_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    url = models.URLField(max_length=MAX_URL_LENGTH)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    # link UserProfile to User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username