from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL
from django import forms

# Create your views here.



class URLForm(forms.ModelForm):

    class Meta:
        model = ShortenedURL
        fields = ['original_url']



def shorten_url(request):

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            shortened_url = form.save()

            return render(request , 'shortener/success.html' , {'short_code' : shortened_url.short_code})

    else:
        form = URLForm()

    return render(request , 'shortener/index.html' , {'form' : form})



def redirect_to_url(request , short_code):

    url_entry = get_object_or_404(ShortenedURL , short_code = short_code)

    return redirect(url_entry.original_url)
