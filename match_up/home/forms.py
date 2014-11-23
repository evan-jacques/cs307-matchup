from django import forms
from .models import UserPicks, Users, Schedule
import datetime
import pytz

class tableForm(forms.Form):
	
	picks = [('Home', 'Home'), ('Away','Away')]
	pick = forms.ChoiceField(choices=picks, widget=forms.RadioSelect())