from django.shortcuts import render
from analysis.views import index as analysis_index

# redirects to upload file
def index(request):
    return analysis_index(request) 

