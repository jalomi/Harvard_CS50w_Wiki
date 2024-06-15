from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    body = util.get_entry(title)
    if not body:
        body = "ERROR: page not found"
        
    return render(request, "encyclopedia/page.html", {
        "page_title": title,
        "content": body,
    })

