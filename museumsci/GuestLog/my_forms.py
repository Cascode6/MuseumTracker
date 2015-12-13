from django import forms
from django.forms import ModelForm
from GuestLog.models import Walk_in, Group
import datetime



#forms based on the models!

class WalkForm(forms.ModelForm):
	class Meta:
		model = Walk_in
		fields = ('Number_of_guests', 'Age', 'Ethnic_background', 'Returning_Guest', 'timestamp')
		widgets = {
			'Number_of_guests': forms.NumberInput(),
			'Age': forms.RadioSelect(choices=Walk_in.AGE_CHOICES),
			'Ethnic_background': forms.RadioSelect(choices=Walk_in.Ethnic_background_choices),
			'timestamp': forms.DateTimeInput(),
		}
		
			


class GroupForm(forms.ModelForm):	
	class Meta:
		model = Group
		fields = ('New_Group', 'Number_of_Teachers', 'Number_of_Chaperones', 'Number_of_Students', 'School', 'Grade', 'Museum_Program', 'timestamp')
		widgets = {
			'Number_of_Teachers': forms.NumberInput(),
			'Number_of_Chaperones': forms.NumberInput(),
			'Number_of_Students': forms.NumberInput(),
			'Grade': forms.Select(choices=Group.GRADE_CHOICES),
			'timestamp': forms.HiddenInput(),
		}
		
		