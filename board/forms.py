from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Board

class PostForm(forms.ModelForm):
    board_content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Board
        fields = ('board_title','board_content','board_file')
        widget = { 
            
            'board_content' : forms.Textarea(attrs={'cols':100, 'rows':100}),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['board_file'].required = False
        self.fields['board_title'].widget.attrs.update({'class':'form-control'})