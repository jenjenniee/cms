from django.db import models
from django.contrib.auth.models import User


class Commute(models.Model):
    COMMUTE_CATEGORY = (
        ('1','출근'),
        ('2','퇴근'),
        ('3','재택출근'),
        ('4','재택퇴근')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commute_category = models.CharField(verbose_name="출근/퇴근",choices=COMMUTE_CATEGORY,max_length=1)
    commute_date = models.DateTimeField(verbose_name='출퇴근시간')
    commute_reason = models.CharField(verbose_name="재택사유", max_length=500,null=True,blank=False)

    def __str__(self):
        return f'{self.user.username}/{self.commute_date}/{dict(self.COMMUTE_CATEGORY).get(self.commute_category)}'
