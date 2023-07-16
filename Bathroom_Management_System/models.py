from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
# 创建用户表
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


# 创建书籍表
class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_time = models.DateTimeField()
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    author = models.ManyToManyField(to='Author')


# 创建出版社表
class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.EmailField()


# 创建作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetails', on_delete=models.CASCADE)


# 创建作者详情表
class AuthorDetails(models.Model):
    addr = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
