from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_time = models.DateTimeField()
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    importance = models.CharField(max_length=20, default='pas_urgent')
    completed = models.BooleanField(default=False)



    def save(self, *args, **kwargs):

        now = timezone.now()
        time_difference = self.due_time - now

        if time_difference.days > 2:
            self.importance = 'pas_urgent'
        elif time_difference.days > 0:
            self.importance = 'peu_urgent'
        else:
            self.importance = 'tres_urgent'

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} - {'Completed' if self.completed else 'Not Completed'}"
