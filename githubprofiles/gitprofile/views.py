from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import login
from gitprofile.forms import UserForm
from django.contrib.auth import get_user_model
from .models import UserProfile,Profile,Repository
from django.contrib.auth.models import User
import requests,datetime
# Create your views here.
def register(request):
	if request.method=="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('home'))
	else:
		form = UserForm()
			
	args={'form':form}
	return render(request,'registration/reg_form.html',args)
def explore(request):
	
	users = User.objects.all().values_list('username',flat=True)
	arg={'users':User.objects.all()}
	return render(request, 'registration/explore.html', arg)
	
def detail(request,ide):
	p=Profile()
	
	if request.method=="GET":
		k=User.objects.get(pk=ide)
		l='https://api.github.com/users/'+k.username
		m=l+'/repos'
		res=requests.get(l)
		r=res.json()
		rep=requests.get(m)
		rep=rep.json()
		p.user=k
		p.followers=r['followers']
		p.pk
		p.repository=[]
		p.save()
		repos=[i['name'] for i in rep]
		stars=[i['stargazers_count'] for i in rep]
		
		for i in range(len(repos)):
			l=Repository(repo=repos[i],star=stars[i],profile=p)
			l.save()	
			p.repository_set.add(l)
	args={'p':p}
	return render(request,'registration/profile.html',args)
def may(request,ide):
	if request.method=="GET":
		k=User.objects.get(pk=ide)
		if Profile.objects.get(user=k):
			p=Profile.objects.get(user=k)
			p.time=datetime.datetime.now()
			return render(request,'registration/profile.html',{'p':p})
		else:
			return detail(request,ide)	

			
	
	
		

