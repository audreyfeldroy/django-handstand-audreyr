from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select
from django.utils.translation import ugettext_lazy as _

from profiles.models import Profile


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('username', 'fullname', 'email', 'email_preference', 'twitter_username', 'fb_username')
        model = Profile
        widgets = {
            'username': TextInput(attrs={'class': 'span4'}),
            'fullname': TextInput(attrs={'class': 'span4'}),
            'email': TextInput(attrs={'class': 'span4'}),
            'email_preference': Select(attrs={'class': 'span6'}),
            'twitter_username': TextInput(attrs={'class': 'span4 disabled', 'readonly': 'readonly'}),
            'fb_username': TextInput(attrs={'class': 'span4 disabled', 'readonly': 'readonly'}),
        }
