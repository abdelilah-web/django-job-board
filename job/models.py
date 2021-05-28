from django.db import models
from django.utils.text import slugify
# Create your models here.

'''
django model field :
    - html widget
    - validation
    - db size
'''
job_type_choices = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    title        = models.CharField(max_length=120)
   # location     = 
    job_type     = models.CharField(
        max_length = 20,
        choices = job_type_choices,
        default = 'Full Time')
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) # take the time by it self
    Vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=0)
    experience   = models.IntegerField(default=1)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)# One to Many
    image        = models.ImageField(upload_to = 'jobs/')

    slug         = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name