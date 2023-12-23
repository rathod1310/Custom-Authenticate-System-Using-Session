from django.db import models

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=50)
	zipcode=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic",default="")
	usertype=models.CharField(max_length=100,default="buyer")

	def __str__(self):
		return self.fname+" "+self.lname