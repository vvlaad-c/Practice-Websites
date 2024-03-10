from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all_posts.html")

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")