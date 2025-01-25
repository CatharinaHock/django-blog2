from django.conf import settings
from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

class Tag(models.Model):
    name = models.CharField(max_length=50)
    background_color = ColorField(default='#000000')
    text_color = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    brief_description = models.TextField(max_length= 1000, default="Unbeschreiblich.")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    main_img = models.ImageField(upload_to='images/', default="images/default.png")
    color_rotation = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    by_me =models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    