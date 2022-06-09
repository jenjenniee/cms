from django.db import models
from django.contrib.auth.models import User

# 일일 보고 
class DailyReport(models.Model):

    class Meta:
        index_together = ['dr_drafter', 'dr_addressee']
        verbose_name = "일일 보고" 
        verbose_name_plural = "일일 보고"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    dr_drafter = models.ForeignKey(User, verbose_name="기안자", on_delete=models.CASCADE, related_name='drafter')
    dr_addressee = models.ForeignKey(User, verbose_name="승인자", on_delete=models.CASCADE, related_name='addressee')
    dr_created_at = models.DateTimeField()
    dr_checked_at = models.DateTimeField(null=True, blank=True)
    dr_status = models.CharField(max_length=10, choices=(('1', '결제대기'), ('2', '승인'), ('3', '반려')))
    dr_title = models.CharField(max_length=100)
    dr_feedback = models.CharField(max_length=5000, null=True, blank=True)
   


# 오늘 업무내용
class DailyContent(models.Model):
    class Meta:
        verbose_name="금일 업무 내용"
        verbose_name_plural="금일 업무 내용"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dc_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    dc_content = models.CharField(max_length=50, null=True)

# 내일 업무계획
class TommrowWill(models.Model):
    class Meta:
        verbose_name="명일 업무 계획"
        verbose_name_plural="명일 업무 계획"
    tw_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    tw_content = models.CharField(max_length=50, null=True)

# 문제점 및 건의사항
class Suggestion(models.Model):
    class Meta:
        verbose_name="문제점 및 건의사항"
        verbose_name_plural="문제점 및 건의사항"
    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    s_content = models.CharField(max_length=50, null=True)
