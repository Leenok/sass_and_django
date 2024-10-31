from django.shortcuts import render

# Create your views here.
def sass_page_handler(request):
    return render(request, 'index.html')
