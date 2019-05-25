from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='project_pics',blank=True)
    user_project_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images

    @classmethod
    def search_project_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    class Meta:
        ordering = ['-id']
    
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField()
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
