from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length= 500)
    image = models.CharField(max_length=100)
    date = models.DateTimeField()
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title