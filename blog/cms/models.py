from django.db import models
from django.template.defaultfilters import slugify
from cms import markdown

class Blog_post(models.Model):
    post_text = models.TextField()
    title = models.CharField(max_length=128)
    title_slug = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.post_text = markdown.parse(self.post_text)
        self.title_slug = slugify(self.title)
        super(Blog_post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title