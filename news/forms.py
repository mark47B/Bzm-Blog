from cProfile import label
from django import forms
from .models import Category, News
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    captcha = CaptchaField(label='')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя', 
        widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
        help_text='Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'
        )
    password1 = forms.CharField(label='Пароль', 
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text=''' 
        <ul> 
        <li>Пароль не должен быть слишком похож на другую вашу личную информацию.</li>
        <li>Ваш пароль должен содержать как минимум 8 символов.</li>
        <li>Пароль не должен быть слишком простым и распространенным.</li>
        <li>Пароль не может состоять только из цифр.</li>
        </ul>'''
        )
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User   
        fields = ('username', 'email', 'password1', 'password2')


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
            raise ValidationError('Заголовок не должен начинаться с цифры!')
        return title
