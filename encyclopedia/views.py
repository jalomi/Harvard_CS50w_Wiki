from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"placeholder":"Title"}))
    content = forms.CharField(label="",
                              widget=forms.Textarea(attrs={"placeholder":"New Page's Content"}))

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

def newPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title in util.list_entries():
                return render(request, "encyclopedia/newpage.html", {
                    "error": "ERROR: Page already exists"
                })
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("page", args=[title]))
        else:
            return render(request, "encyclopedia/newpage.html", {
                "error": "ERROR: Invalid input"
            })
    else:
        return render(request, "encyclopedia/newpage.html", {
            "form": NewPageForm()
        })
