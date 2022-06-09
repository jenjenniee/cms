from dataclasses import field
from django import forms

from notice.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['title', 'hook_text', 'content', 'file_upload', 'category']
        # field_classes = {
        #     'file_upload': forms.FileField
        # }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hook_text': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            #  'head_image': forms.FileInput(attrs={'class': 'form-control input_box', 'accept': 'image/*'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'title': '제목',
            'hook_text' : '소제목',
            'content': '내용',
            'file_upload' : '파일',
            'imgs': '이미지',
            'category': '카테고리',
        }