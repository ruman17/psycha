from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import QResponseForm
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def post_new(request):
	# form = QResponseForm(request.POST)
	# form.is_valid()
	dob = datetime.datetime.strptime(request.POST.get('p_dob'), '%Y-%m-%dT%H:%M:%S.%fZ')
	data = {
	'p_dob': dob,
	'p_f_name': request.POST.get('p_f_name'),
	'p_l_name': request.POST.get('p_l_name'),
	'response_array': request.POST.get('response_array')
	}
	# print(datetime.datetime.strptime(request.POST.get('p_dob'), '%Y-%m-%dT%H:%M:%S.%fZ')) 
	form = QResponseForm(data)
	# form.cleaned_data['pub_date'] = timezone.now()
	# print(form.cleaned_data)
	# form.save()
	# form.cleaned_data['pub_date'] = timezone.now
	if form.is_valid():
		poll_result = form.save(commit=False)
		poll_result.save()
		return HttpResponse("success")
	else:
		print(form.errors)
		return HttpResponse(form)