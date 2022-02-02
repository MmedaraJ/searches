from logging import PlaceHolder
from django import forms
from .models import *

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "gender", "image", "sport"]
    
    def clean(self):
        super(UsersForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        image = self.cleaned_data.get('image')

        if len(first_name)<1:
            self.errors['first_name'] = self.error_class(["First name cannot be empty"])
        elif len(first_name)<2:
            self.errors['first_name'] = self.error_class(["First name must contain at least two letters"])

        if len(last_name)<1:
            self.errors['last_name'] = self.error_class(["Last name cannot be empty"])
        elif len(last_name)<2:
            self.errors['last_name'] = self.error_class(["Last name must contain at least two letters"])
        
        if len(image)<1:
            self.errors['image'] = self.error_class(["Image link cannot be empty"])

        return self.cleaned_data


class FilterForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female')
    )
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, widget=forms.CheckboxSelectMultiple)
    Basketball = 'basketball'
    Football = 'football'
    Baseball = 'baseball'
    Cricket = 'cricket'
    Hockey = 'hockey'
    SPORT_CHOICES = (
        (Basketball, 'Basketball'),
        (Football, 'Football'),
        (Baseball, 'Baseball'),
        (Cricket, 'Cricket'),
        (Hockey, 'Hockey')
    )
    sport = forms.MultipleChoiceField(label='Sports', choices=SPORT_CHOICES, widget=forms.CheckboxSelectMultiple)