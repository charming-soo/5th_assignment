from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects
    return render(request, 'home.html', {'portfolios': portfolios})

def detail(request, portfolio_id):
    details = get_object_or_404(Portfolio, pk = portfolio_id)
    return render(request, 'detail.html', {'details':details})
