from django.shortcuts import render

# redirects to page with file upload
def index(request):
    return render(request, 'analysis/file_upload.html', {})
