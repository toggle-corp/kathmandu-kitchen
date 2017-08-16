from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class Post(models.Model):
    header_image = models.FileField(upload_to='blog_images',
                                    null=True, blank=True, default=None)
    title = models.CharField(max_length=300)
    content = HTMLField()
    slug = models.SlugField(default=None, null=True, blank=True)

    created_by = models.ForeignKey(User, related_name="created_posts")
    created_at = models.DateTimeField(auto_now_add=True)

    modified_by = models.ForeignKey(User, related_name="modified_posts")
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-modified_at']
