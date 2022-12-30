from django.shortcuts import redirect, render  
from django.core.files.storage import FileSystemStorage
from .models import fakeDetector
import os

def index(request):
    if request.method == 'POST':
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        file_url = os.path.abspath(file)
        res = fakeDetector(file_url)
        if(res):
            return render(request, 'next.html', {'result': 'The Logo is Real'})
        else:
            return render(request, 'next.html', {'result': 'The Logo is Fake'})
    
    return render(request, 'index.html')