from django.shortcuts import render
from .models import BlackCard
# Create your views here.
from django.http import HttpResponse

def home(request):
	black_card = BlackCard.objects.all()
	return render(request, 'index.html',{'black_card':black_card})



