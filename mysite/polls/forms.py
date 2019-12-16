from django.db import models
from django.forms import ModelForm
from .models import QResponses
from django import forms
from django.conf import settings
from django.utils import timezone
import datetime


class QResponseForm(forms.ModelForm):
	# pub_date =  forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S.%fZ"])
	def clean(self):
		cleaned_data = super(QResponseForm, self).clean()
		# here all fields have been validated individually,
		# and so cleaned_data is fully populated
		print(cleaned_data)
		# p_dob = datetime.datetime.strptime(cleaned_data.get('p_dob'), '%Y-%m-%dT%H:%M:%S.%fZ')  
		# pub_date =  timezone.now()
		return cleaned_data
	class Meta:
		model = QResponses
		fields = ('response_array','p_f_name','p_l_name','p_dob')
