from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
class News(models.Model):
    title=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='images')
    video=models.FileField(upload_to='videos',null=True,blank=True)
    description=models.TextField()
    read_count=models.PositiveIntegerField(default=0)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.category} / {self.title}'
    
    class Meta:
        verbose_name_plural = "News"
    

    