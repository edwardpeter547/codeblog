from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.fullname
    

class Setting(models.Model):
    sitename = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    github = models.CharField(max_length=255, null=True)
    
    class Meta:
        verbose_name_plural  = "Website Settings"
        
    
    def __str__(self):
        return f"{self.sitename} - Settings"
