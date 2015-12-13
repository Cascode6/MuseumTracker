from django.db import models
import datetime
import django.forms as forms


# class Walk_inManager(models.Manager):
# 	def create_record(self, Age, Number_of_guests, Ethnic_background, Returning_Guest, timestamp):
# 		record = self.create(Age=Age, Number_of_guests=Number_of_guests, Ethnic_background=Ethnic_background, Returning_Guest=Returning_Guest, timestamp=timestamp)
# 		return record
# 
# class GroupManager(models.Manager):
# 	def create_group(self, New_Group, Number_of_Teachers, Number_of_Chaperones, Number_of_Students, School, Grade, Museum_Program, timestamp):
# 		record = self.create( New_Group=New_Group, Number_of_Teachers=Number_of_Teachers, Number_of_Chaperones=Number_of_Chaperones, Number_of_Students=Number_of_Students, School=School, Grade=Grade, Museum_Program=Museum_Program, timestamp=timestamp)		
# 		return record
# 



# Create your models here.
class Walk_in(models.Model):
	S = "Senior"
	A = "Adult"
	T = "Teen"
	C = "Child"
	AGE_CHOICES = (
		(S, "Senior"),
		(A, "Adult"),
		(T, "Teen"),
		(C, "Child")
	)
	
	I = "Indian"
	B = "Black"
	W = "White"
	L = "Latin-American"
	K = "Asian"
	Ethnic_background_choices = (
		(I, "Indian"),
		(B, "Black"),
		(W, "White"),
		(L, "Latin-American"),
		(K,  "Asian"),
	)

	Number_of_guests = models.IntegerField()
	Age = models.CharField(max_length = 10, choices=AGE_CHOICES)
	Ethnic_background = models.CharField(max_length = 15, choices=Ethnic_background_choices)
	Returning_Guest = models.BooleanField()
	timestamp = models.DateTimeField(default=datetime.datetime.now)
	

	
class Group(models.Model):
	F = "1"
	S = "2"
	T = "3"
	Y = "4"
	M = "Middle"
	H = "High"
	GRADE_CHOICES = (
		(F, "First"),
		(S, "Second"),
		(T, "Third"),
		(Y, "Fourth"),
		(M, "Middle School"),
		(H, "High School")
	)
	
	New_Group = models.BooleanField()
	Number_of_Teachers = models.IntegerField()
	Number_of_Chaperones = models.IntegerField()
	Number_of_Students = models.IntegerField()
	School = models.CharField(max_length = 15) #add choices dynamically?
	Grade = models.CharField(max_length = 1, choices = GRADE_CHOICES)
	Museum_Program = models.CharField(max_length = 3) #add choices dynamically
	timestamp = models.DateTimeField(default=datetime.datetime.now)