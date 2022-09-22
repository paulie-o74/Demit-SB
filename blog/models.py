from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """
    All details of the post model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        """
        Meta class for ordering
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        To return it's title
        """
        return self.title


class Comment(models.Model):
    """
    All details of the comment model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        """
        Meta class for ordering
        """
        ordering = ['created_on']

    def __str__(self):
        """
        To return a string
        """
        return 'Comment {} by {}'.format(self.body, self.name)
