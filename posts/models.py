
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager



# Create your models here.
class card(models.Model):
    STATUS_CHOICES = (
        ('0' , 'Draft'),
        ('1',  'Published'),
    )
    title   = models.CharField(max_length=255)
    body    = models.TextField()
    img     = models.ImageField(upload_to = 'post/')
    image   = models.ImageField(upload_to = 'post/')
    genre   = models.CharField(max_length=225)
    Written_by = models.CharField(max_length=225)
    Created_by = models.CharField(max_length=225)
    Release_dates = models.CharField(max_length=225)
    Language = models.CharField(max_length=225)
    slug    = models.SlugField(max_length=225, unique_for_date='published_at')
    author  = models.ForeignKey( User, on_delete=models.CASCADE)
    status  = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    tags = TaggableManager()
    imdb = models.CharField(max_length=225 ,blank=True )
    best_series = models.CharField(max_length=225 ,blank=True)
    best_film = models.CharField(max_length=225, blank=True)


    published_at = models.DateTimeField(default=timezone.now)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post:post_view", kwargs={
            "year": self.published_at.year,
            "month": self.published_at.month,
            "day": self.published_at.day,
            "slug": self.slug,

            })


class Comment(models.Model):
    post = models.ForeignKey(card, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"comment by {self.name} on {self.post}"


    