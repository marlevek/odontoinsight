from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    """Home page - landing ou login"""
    if request.user.is_authenticated:
        return render(request, 'core/dashboard.html')
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    """Dashboard principal"""
    context = {
        'page_title': 'Dashboard',
    }
    return render(request, 'core/dashboard.html', context)
