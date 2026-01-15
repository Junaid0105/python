from django.shortcuts import render

# Create your views here.
def all_junaid(request):
    return render(request, 'junaid/all_junaid.html')