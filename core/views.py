from django.shortcuts import render
from .models import BlackCard, WhiteCard
# Create your views here.
from django.http import HttpResponse

def home(request):
	black_card = BlackCard.objects.all()
	white_card = WhiteCard.objects.all()
	
	return render(request, 'index.html',{
		'black_card':black_card,
		 'white_card':white_card})

def cardsPage(request):
	return render(request, 'card_game.html')


