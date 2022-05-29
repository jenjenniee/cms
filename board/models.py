from django.db import models
from django.contrib.auth.models import User

#게시판
class Board(models.Model):


    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False,verbose_name="작성자")
    category = models.CharField(max_length=100,null=True,blank=True)
    board_title = models.CharField(max_length=100,null=True,blank=False,verbose_name="게시판 제목")
    board_content = models.TextField(max_length=500,null=True,blank=False,verbose_name="내용")
    board_date = models.DateTimeField(null=True,blank=False, verbose_name="작성일")
    board_hits = models.IntegerField(default=0,verbose_name="조회수")
    board_file = models.FileField(null=True,blank=True, verbose_name="파일")

    def __str__(self):
        return self.board_title