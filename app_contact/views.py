from django.shortcuts import render

# Create your views here.
def aff_contact(request):
    return render(request,"contact.html")