from django.contrib import admin
from .models import Walk_in
from .models import Group


#register Walk_in model's datafields:
class Walk_inAdmin(admin.ModelAdmin):
	fields = ['NUM', 'AGE', 'ETHNO', 'NEW_G']
#register the Entry model:
admin.site.register(Walk_in)


class GroupAdmin(admin.ModelAdmin):
	fieldset = ['NEW_GR', 'N_TEACHER', 'N_CHAPERONE', 'N_STUDENT', 'SCHOOL', 'GRADE']

admin.site.register(Group)


# #Ethnicity's fields:
# class EthnicityAdmin(admin.ModelAdmin):
# 	fields = ['ethno', 'guests']
# admin.site.register(Ethnicity)

#both for Demographic:
# class DemographicAdmin(admin.ModelAdmin):
# 	fields = ['vis_date', 'age_guest', 'new']
# admin.site.register(Demographic)