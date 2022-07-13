from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    first_name=models.CharField('First Name',max_length=100)
    last_name=models.CharField('Last Name',max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,null=True)
    college_name=models.CharField('College Name',max_length=50)
    total_vote = models.IntegerField(default=0, editable=False,null=True)
    student_id=models.CharField('Student id',max_length=50)
    phone_number=models.CharField('Phone Number',max_length=50)
    e_mail=models.EmailField('E-Mail', max_length=50,blank=True)
    adhaar_card_no=models.CharField('Adhaar Card Number',max_length=50)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Voters(models.Model):
    username =  models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    first_name=models.CharField('First Name',max_length=100)
    last_name=models.CharField('Last Name',max_length=100)
    student_id=models.CharField('Student id',max_length=50)
    adhaar_card_no=models.CharField('Adhaar Card Number',max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class ControlVote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.voter, self.position, self.status)
