from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'dataStorage'
urlpatterns = [
	#path('/', login_required(iViews.familyList.as_view()), name='familyList'),
	path('', views.home, name='home'),
]