from django.shortcuts import render

# Create your views here.

# Views to docs
def docs(request):
    return render(request, 'api_docs/comment_api/comment_doc.html')

# def docs(request):
#     return render(request, 'api_docs/auth_api/auth_doc.html')

# Views to hire consultant
def consultant(request):
    return render(request, 'api_docs/comment_api/api_hire_consultant.html')

