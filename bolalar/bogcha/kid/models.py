
from django.db import models

class Category(models.Model):
    rank=models.CharField(max_length=50, null=True)
    description=models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.rank

class Staff(models.Model):

    name=models.CharField(max_length=50, null=True)
    lastname=models.CharField(max_length=50, null=True)
    image=models.ImageField(null=True)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Group(models.Model):
    name=models.CharField(max_length=50, null=True)
    number_of_children=models.IntegerField(null=True)
    teacherName=models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Children(models.Model):
    name=models.CharField(max_length=50, null=True)
    lastname=models.CharField(max_length=70, null=True)
    age=models.IntegerField(null=True)
    group=models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blogId=models.IntegerField(null=True)
    head=models.CharField(max_length=250, null=True)
    body=models.TextField(null=True)
    image=models.ImageField(null=True, blank=True)
    autor=models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.head


class EatingTime(models.Model):
    name=models.CharField(max_length=50, null=True)
    time=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Meals(models.Model):
    name=models.CharField(max_length=100, null=True)
    drink=models.CharField(max_length=50, null=True)
    day=models.CharField(max_length=50, null=True)
    chef=models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    time=models.ForeignKey(EatingTime, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.day

class Gallery(models.Model):
    picture=models.ImageField(null=True)
    imgId=models.IntegerField(null=True)
    owner=models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.imgId)

class Contact(models.Model):
    name=models.CharField(max_length=50, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField()

    def __str__(self):
        return self.email