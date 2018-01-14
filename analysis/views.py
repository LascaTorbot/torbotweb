from django.shortcuts import render
from django.conf import settings
import requests

# redirects to page with file upload
def index(request):
    return render(request, 'analysis/file_upload.html', {})

def submit_files(request):
    email = request.POST['email']

    for fin in request.FILES.getlist("files"):
        submit_url = settings.AQUARI_URL + 'submit_web'

        files = {'file': fin}
        data = {
            'args': '--machine win7',
            'email': email,
            'filename': fin.name
        }
        r = requests.post(submit_url, files=files, data=data)

    return index(request)
