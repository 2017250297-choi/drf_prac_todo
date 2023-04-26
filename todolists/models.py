from django.db import models

# import time
from django.utils import timezone


# Create your models here.
class TodoList(models.Model):
    class Meta:
        db_table = "todolist_table"

    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True, blank=True)
    # user_id = models.ForeignKey()

    def save(self, *args, **kwargs):
        if self.is_complete:
            self.completion_at = timezone.now()
        else:
            self.completion_at = None
        super().save(*args, **kwargs)
