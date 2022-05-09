from django.db import models

# Create your models here.


class Jobs(models.Model):

    # type: varchar(11)
    # - url: varchar(100)
    # - title: varchar(100)
    # - description: text
    # - how_to_apply: text (
    job_type = models.CharField(max_length=11)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    how_to_apply = models.TextField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.job_type} - {self.url} - {self.title} - {self.description} - {self.how_to_apply}"
