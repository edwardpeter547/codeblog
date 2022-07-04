from django.db import models

# Create your models here.


class Category(models.Model):
    title  = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug
    
    

class Post(models.Model):
    
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS = (
        (ACTIVE, 'Active'), 
        (DRAFT, 'Draft')
    )
    
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Comments"
    
    
    def __str__(self):
        return f"{self.post.title} - {self.fullname}"