from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

#class-based view construction
from django.views.generic.dates import MonthArchiveView

#python modules for data display and file output
import datetime
import csv

#bring in the models!
from .models import Walk_in, Group
from .my_forms import WalkForm, GroupForm

#View Classes - experimental



#Inex containing link (in html) to walkform and group form
def index(request):
	#I want all entries as of now
	date = datetime.datetime.now()
	
	template = loader.get_template('GuestLog/index.html')
	context = RequestContext(request, {
		'date' : date,
		})
	return HttpResponse(template.render(context))
	
def walkform(request):
	if request.method == 'POST':
		form = WalkForm(request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/GuestLog/')
		
	else:
		form = WalkForm()
		
	return render(request, 'walkform.html', {'form' : form})
	
def groupform(request):
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/GuestLog/')
		
	else:
		form = GroupForm()
	return render(request, 'groupform.html', {'form' : form})


def create_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="MuseumAttendanceData.csv"'
	
	table = Walk_in.objects.all().values()
	
	writer = csv.writer(response)
	for row in table:
		writer.writerow(list(enumerate(row)))
	return response