from django.db import models


class Courses(models.Model):
	semester_text = models.CharField(max_length = 100)  
	crn = models.IntegerField(default = 100)
	subject = models.CharField(max_length = 100)
	course_Number = models.IntegerField(default = 100)
	section = models.IntegerField(default = 100)
	title = models.CharField(max_length = 100)


