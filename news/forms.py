from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control' }),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows': 4 }),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category' : forms.Select(attrs={'class':'form-control' })
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError('Title starts with number :(')
        return title
