from django.shortcuts import render
from django.utils import timezone
from .models import fback
from .forms import FbackForm


# Create your views here.
def main_page(request):
    return render(request, 'cryptapp/main_page.html', {})

def system_feature(request):
    return render(request, 'cryptapp/system_feature.html', {})

def about_us(request):
    return render(request, 'cryptapp/about_us.html', {})

def system(request):
    return render(request, 'cryptapp/system.html', {})

def issues(request):
    return render(request, 'cryptapp/issues.html', {})

def contact(request):
    return render(request, 'cryptapp/contact.html', {})

def feedback(request):
    if request.method == 'POST':
        form = FbackForm(data=request.POST)
        if form.is_valid():
            fb = form.save(commit = False)
            fb.published_date = timezone.now()
            fb.save()
            
    else:
        form = FbackForm()
    return render(request, 'cryptapp/feedback.html', {'form': form})