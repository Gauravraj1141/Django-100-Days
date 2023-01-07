from django.db import models

from django.contrib.auth.models import User


# Modelraltionship with example and how to query for these particular


# One to One field
# related_name = we gave related name for filter these page when we apply filter so we use this related name for this table

class SinglePage(models.Model):
    P_id = models.AutoField(primary_key=True)
    Page_name = models.CharField(max_length=44)
    Page_date = models.DateField()
    Page_author = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="mypage")


# one to many (foreign_key)z

class Blog(models.Model):
    B_id = models.AutoField(primary_key=True)
    Blog_name = models.CharField(max_length=44)
    Blog_pub_date = models.DateField()
    Blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="myblog")


# ManyToManyField


class Book(models.Model):
    Bk_id = models.AutoField(primary_key=True)
    Book_name = models.CharField(max_length=44)
    Book_pub_date = models.DateField()
    Book_price = models.IntegerField()
    Book_authors = models.ManyToManyField(User,  related_name="mybook")

    def author_names(self):
        return ",".join([str(name) for name in self.Book_authors.all()])
