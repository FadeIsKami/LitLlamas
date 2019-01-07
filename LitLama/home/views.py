from django.shortcuts import render


updates = [
    {
        "author": "Fade",
        "title": "Patch notes 1.0.0",
        "content": "Major Changes",
        "date_posted": "August 27, 2018"
    },
    {
        "author": "Bodom",
        "title": "Patch notes 1.0.1",
        "content": "Minor Changes",
        "date_posted": "August 27, 2018"
    }
]




def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def news(request):
    context = {
        "updates": updates
    }
    return render(request, "home/news.html", context)



