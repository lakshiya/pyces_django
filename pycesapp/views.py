from django.shortcuts import render, redirect
import re 
import requests

# Create your views here.
from .forms import FileUploadForm
from django import forms

def file_upload(request):
    error_message = ""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            if form.cleaned_data['zipfile']:
                
                print(form.cleaned_data['zipfile'].name)
                if form.cleaned_data['zipfile'].name.endswith(".zip"):
                    return redirect('file_upload_success')
                else:
                    error_message = "Provide a valid .zip file"
                    # raise forms.ValidationError("Provide a .zip file")
                
            elif form.cleaned_data['repo_link']:
                print(form.cleaned_data['repo_link'])

                if checkRepo(form.cleaned_data['repo_link']):
                    if repoPublic(form.cleaned_data['repo_link']):
                        return redirect('file_upload_success')
                    else:
                        error_message = "Unable to access GitHub project, Please check URL or make the repository Public"
                else:
                    error_message = "Provide a valid GitHub repository URL"
            
            elif form.cleaned_data['cloud_url']:
                checkCloudLoc(form.cleaned_data['cloud_url'])
            
            print(form.cleaned_data['zipfile'])
            uploaded_file = form.cleaned_data['zipfile']

            # Check if File is a .Zip file
            
            # return redirect('file_upload_success')
    else:
        form = FileUploadForm()
    return render(request, 'pycesapp/file_upload.html', {'form': form, 'error_message': error_message})

def file_upload_success(request):
    return render(request, 'pycesapp/file_upload_success.html')

def file_upload_failure(request):
    return render(request, 'pycesapp/file_upload_failure.html')

def checkRepo(repo_link):
    github_url_pattern = re.compile(r'^https?://(www\.)?github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+/?$')

    return bool(github_url_pattern.match(repo_link))

def repoPublic(repo_link):
    URL = repo_link.split('/')
    username = URL[-2]
    repo_name = URL[-1].rstrip('.git')

    github_api_url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.get(github_api_url)

    if response.status_code == 200:
        repo_info = response.json()
        return not repo_info['private']
    else:
        # If the request is not successful, assume the repository is private
        return False

