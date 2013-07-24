#encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	context = {
		'form': form,
	}
	template_name = 'accounts/signup.html'
	return render(request, template_name, context)