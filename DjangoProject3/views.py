from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')

def applicants_view(request):
    return render(request, 'applicants.html')