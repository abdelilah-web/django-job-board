from django.db import models

# Create your models here.

'''
django model field :
    - html widget
    - validation
    - db size
'''
job_type_choices = (
    ('1', 'Full Time'),
    ('2', 'Part Time'),
)

class Job(models.Model):
    title        = models.CharField(max_length=120)
   # location     = 
    job_type     = models.CharField(
        max_length = 20,
        choices = job_type_choices,
        default = '1')
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) # take the time by it self
    Vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=0)
    experience   = models.IntegerField(default=1)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)# One to Many

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name