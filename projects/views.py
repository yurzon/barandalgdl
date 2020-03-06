from django.shortcuts import render

def project_index(request):
    return render(request, 'projects.html')

def project_detail(request):
    return render(request, 'project_details.html')
