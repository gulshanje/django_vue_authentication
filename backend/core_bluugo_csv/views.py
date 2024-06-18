from django.shortcuts import render

# Create your views here.

def upload_file_view(request):
    return render(request,'core_bluugo_csv/upload.html', {})