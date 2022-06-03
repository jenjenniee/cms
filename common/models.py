from tkinter import PhotoImage
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, verbose_name="프로필 사진", upload_to="profile/")
    user_department = models.CharField(max_length=20, null=True,blank=True, verbose_name="부서")
    user_rank= (('1','과장'),
    ('2','차장'),
    ('3','대리'),
    ('4','주임'),
    ('5','사원')
    )
        
    def __str__(self):
        return self.user.username
