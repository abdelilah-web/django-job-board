from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    owner        = models.ForeignKey(User, name='owner', on_delete=models.CASCADE)
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


class Apply(models.Model):
    job          = models.ForeignKey(Job,related_name='apply_job', on_delete= models.CASCADE)
    name         = models.CharField(max_length=25)
    email        = models.EmailField(max_length=100)
    website      = models.URLField()
    upload_cv    = models.FileField(upload_to='apply/')
    cover_leter  = models.TextField(max_length=500)
    created_at   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name