from django.shortcuts import render

def main_page(request):
    return render(request, 'pages/main.html')
'''
def lents_page(request):
    return render(request, 'pages/lents.html')

def videolents_page(request):
    return render(request, 'pages/videolents.html')
'''
def forum_page(request):
    return render(request, 'pages/forum.html')

def cloud_page(request):
    return render(request, 'pages/cloud.html')

def auth_error(request):
    return render(request, 'pages/authorizade_error.html')