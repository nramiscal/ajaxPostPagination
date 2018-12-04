from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Post id: {self.id} '{self.post}'>"