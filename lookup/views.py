from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name="lookup/home.html")

def about(request):
    return render(request, template_name="lookup/about.html")