from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, get_resolver
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_out, user_logged_in, user_login_failed
from django.dispatch import receiver

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
	messages.info(request, '['+request.user.username+'] Logged out.')

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
	messages.success(request, '['+request.user.username+'] Logged in.')

@receiver(user_login_failed)
def on_user_login_failed(sender, request, **kwargs):
	messages.warning(request, 'Logged in failed.')

@login_required
def home(request):
	context = {}
	#messages.info(request, 'Information')
	#messages.success(request, 'Successful')
	#messages.warning(request, 'Warning')
	return render(request, 'home.html', context)