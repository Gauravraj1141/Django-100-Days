from django.db import models
from django.contrib.auth.models import User


# here we are going to see how we can create one to many relationship we call it foreign key

class Notes(models.Model):
    n_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=44)
    date = models.DateField(auto_now_add=True)
    note = models.CharField(max_length=44)

    # use cascade for when user delete then it notes table will also delte
    # student = models.ForeignKey(User, on_delete=models.CASCADE)
    # use protect so till our notes table will not delete user can't delete
    # student = models.ForeignKey(User, on_delete=models.PROTECT)
    # here if user will delte then place of user set will null and table will not delete
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
