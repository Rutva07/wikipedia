from django.shortcuts import render
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    if name in util.list_entries():     
        return render(request, "encyclopedia/entry.html", {
            "data": markdown2.markdown(util.get_entry(name)),
            "name":name})
    else: 
        return render(request, "encyclopedia/error.html")
    
    
def wikiEntry(request, name):
    if name in util.list_entries():     
        return render(request, "encyclopedia/entry.html", {
            "data": markdown2.markdown(util.get_entry(name)),
            "name":name})
    else: 
        return render(request, "encyclopedia/error.html")
  
    
def search(request):
    if request.method == "POST":
        search_value = request.POST.get('q')
        if search_value in util.list_entries():     
            return render(request, "encyclopedia/entry.html", {
                "data": markdown2.markdown(util.get_entry(search_value)),
                "name":search_value
                })
        elif any(search_value in element for element in util.list_entries()):
            entries = util.list_entries()
            list = [element for element in entries if search_value in element]
            return render(request, "encyclopedia/searching.html", {
                "name": search_value,
                "list": list
            })          
        else: 
            return render(request, "encyclopedia/error.html")
    else:
        entries = util.list_entries()
        return render(request, "encyclopedia/index.html", {'entries': entries})
 
    
def create(request):
    return render(request, "encyclopedia/create.html")


def created(request):
    if request.method == "POST":
        title = request.POST.get("titlef")
        information = request.POST.get("info")
        if title in util.list_entries():
            return render(request, "encyclopedia/error2.html")
        else:
            util.save_entry(title, information)
            return render(request, "encyclopedia/entry.html", {
                "data": markdown2.markdown(util.get_entry(title)),
                "name":title})
   
            
def edit(request, name):
    return render(request, "encyclopedia/edit.html", {
        "data": util.get_entry(name),
        "name":name})      
   
    
def save(request):
    if request.method == "POST":
        data = request.POST.get("infor")
        name = request.POST.get("name")
        util.save_entry(name, data)
        return render(request, "encyclopedia/entry.html", {
                "data": markdown2.markdown(util.get_entry(name)),
                "name":name})
 
        
def get_random(request):
    entries = util.list_entries()
    random_item = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
                "data": markdown2.markdown(util.get_entry(random_item)),
                "name":random_item})
    