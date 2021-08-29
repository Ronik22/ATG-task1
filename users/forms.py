from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget

class UserRegisterForm(UserCreationForm):
    captcha = MathCaptchaField(widget=MathCaptchaWidget(question_class="text-muted mr-2"))
    class Meta:
        model = User
        fields = ['username','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
