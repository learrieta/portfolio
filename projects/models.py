from django.db import models
import uuid
from embed_video.fields import EmbedVideoField

# Create your models here.


#Create Class
class Feature_Project(models.Model):
    #attributes
    #owner
    title = models.CharField(max_length=200)
    overview = models.TextField(null = True, blank = True)
    role = models.CharField(max_length=200,null = True, blank = True)
    team = models.CharField(max_length=200,null = True, blank = True)
    duration = models.CharField(max_length=200,null = True, blank = True)
    quick_description = models.TextField(null = True, blank = True)
    feature_image = models.ImageField(null=True, blank=True, default="coming_soon.png")
    feature_video = EmbedVideoField(null=True, blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    development = models.ManyToManyField('Development_Enviroment', blank=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.title
    
    @property
    def imageUrl(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''

        return img
    
class Project(models.Model):
    #attributes
    #owner
    title = models.CharField(max_length=200)
    overview = models.TextField(null = True, blank = True)
    role = models.CharField(max_length=200,null = True, blank = True)
    team = models.CharField(max_length=200,null = True, blank = True)
    duration = models.CharField(max_length=200,null = True, blank = True)
    quick_description = models.TextField(null = True, blank = True)
    feature_image = models.ImageField(null=True, blank=True, default="coming_soon.png")
    feature_video = EmbedVideoField(null=True, blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    development = models.ManyToManyField('Development_Enviroment', blank=True)

    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.title
    
    @property
    def imageUrl(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''

        return img
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,
                           primary_key=True, editable= False)
    
    def __str__(self):
        return self.name
    

class Development_Enviroment(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,
                           primary_key=True, editable= False)
    
    def __str__(self):
        return self.name
    
