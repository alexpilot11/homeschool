from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from homeschool_site.models import HomeSchoolUser


class HomeSchoolUserCreationForm(UserCreationForm):
    class Meta:
        model = HomeSchoolUser
        fields = ("username", "status")


class HomeSchoolUserChangeForm(UserChangeForm):
    class Meta:
        model = HomeSchoolUser
        fields = '__all__'


class RSVPForm(forms.Form):
    GUEST_CHOICES = [(0, 0), (1, 1), (2, 2)]

    response = forms.BooleanField(required=True)
    num_guests = forms.ChoiceField(choices=GUEST_CHOICES, required=False)
    rsvp_note = forms.CharField(max_length=1000, required=False)

