from django.shortcuts import render
from django.utils import timezone
from .models import fback
from .forms import FbackForm
from .forms import SystemForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import re


# Create your views here.
def main_page(request):
    return render(request, 'cryptapp/main_page.html', {})

def result(request):
    return render(request, 'cryptapp/result.html', {})

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

def thanks(request):
	return render(request, 'cryptapp/thanks.html', {})

def feedback(request):
    if request.method == 'POST':
        form = FbackForm(data=request.POST)
        if form.is_valid():
            fb = form.save(commit = False)
            fb.published_date = timezone.now()
            fb.save()
            return HttpResponseRedirect('/thanks/') 
    else:
        form = FbackForm()
    return render(request, 'cryptapp/feedback.html', {'form': form})


def system(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SystemForm(data=request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            fb = form.save(commit = False)
            fb.save()
            cd = form.cleaned_data

            #vcipher=valid_cipher(cd.get('cipher'))
            #return render_to_response('cryptapp/system_feature.html',{'form':form})
            #return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SystemForm()

    return render(request, 'cryptapp/system.html', {'form': form})

#to check whether cipher is valid or not
# def valid_cipher(c):
#     res=""
#     match = re.match(r'^[A-Za-z ]*$', c)
#     if not match:
#         res="Invalid CipherText"
#     else:
#         res="Valid CipherText"
#     return res