from django.shortcuts import render

# Create your views here.

def api_view(request):
    template_name = "comment_doc"
    js_link = "<script src=assets/path/file.js></script>"
    return render(
        request,
        "api_docs/comment_api/comment_doc.html",
        {'template_name': template_name, 'js_link': js_link}
    )

