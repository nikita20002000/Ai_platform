from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Image

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", 'first_name', 'last_name')
    # confirmation = forms.BooleanField(widget=forms.RadioSelect(attrs={"class": "form-control;"}))
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control;"}))
    #
    # def clean_confirmation(self):
    #     if self.cleaned_data["confirmation"] is not True:
    #         raise ValidationError("You must confirm!")


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')
