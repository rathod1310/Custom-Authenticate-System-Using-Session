from django.shortcuts import render,redirect
from .models import *
from .models import User

def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			return render(request,'applicant_home.html')
		else:
			return render(request,'company_home.html')
	except:
		return render(request,'index.html')

def company_home(request):
	user=User.objects.get(email=request.session['email'])
	return render(request,'company_home.html',{'user':user})

def applicant_home(request):
	user=User.objects.get(email=request.session['email'])
	return render(request,'applicant_home.html',{'user':user})


def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						city=request.POST['city'],
						state=request.POST['state'],
						zipcode=request.POST['zipcode'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
						usertype=request.POST['usertype']
					)
				msg="User Sign Up Successfully"
				return render(request,'signin.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def signin(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return redirect('applicant_home')
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'company_home.html')
			else:
				msg="Incorrect Password"
				return render(request,'signin.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signin.html')

def signout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'index.html')
	except:
		return render(request,'index.html')
	

def change_password(request):
    user = User.objects.get(email=request.session['email'])
    
    if request.method == "POST":
        if user.password == request.POST['old_password']:
            if request.POST['new_password'] == request.POST['cnew_password']:
                user.password = request.POST['new_password']
                user.save()

                # Check usertype and redirect accordingly
                if user.usertype=="buyer":
                    return redirect('applicant_home')
                elif user.usertype=="seller":
                    return redirect('company_home')
                else:
                    # Handle other usertypes if needed
                    return redirect('signout')
            else:
                msg = "New Password & Confirm New Password Do Not Match"
        else:
            msg = "Old Password Does Not Match"

        if user.usertype == "buyer":
            return render(request, 'change_password.html', {'msg': msg})
        else:
            return render(request, 'change_password.html', {'msg': msg})
    else:
        if user.usertype == "buyer":
            return render(request, 'change_password.html')
        else:
            return render(request, 'change_password.html')
