from django.db import models

class Blog_post(models.Model):
    post_text = models.TextField()
    title = models.CharField(max_length=128)
    title_slug = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog_post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title