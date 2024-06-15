from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

def search(request):
    query = request.GET.get("q")

    if query in util.list_entries():
        return HttpResponseRedirect(reverse("page", args=[query]))
    
    results = []

    for entry in util.list_entries():
        if query.lower() in entry.lower():
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results,
    })

