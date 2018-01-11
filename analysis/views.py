from django.shortcuts import render
from django.conf import settings
from utils.hash import file_hash

# redirects to page with file upload
def index(request):
    return render(request, 'analysis/file_upload.html', {})

def submit_files(request):
    for fin in request.FILES.getlist("files"):
        print(file_hash(fin))

    return index(request)
