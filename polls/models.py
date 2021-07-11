from django.db import models
from user.models import CustomUser


# Create your models here.
class PollQuestion(models.Model):
    question = models.TextField(max_length=250)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    option_one = models.CharField(max_length=250, null=False)
    option_two = models.CharField(max_length=250, null=False)
    option_three = models.CharField(max_length=250, null=False)
    option_four = models.CharField(max_length=250, null=False)
    option_one_votes = models.IntegerField(default=0)
    option_two_votes = models.IntegerField(default=0)
    option_three_votes = models.IntegerField(default=0)
    option_four_votes = models.IntegerField(default=0)
