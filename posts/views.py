from django.shortcuts import render
from .models import Post
from Component.views import select_component, create_component, component_list, gpu_detail, cpu_detail, motherboard_detail, psu_detail

# Create your views here.
def index(request):
    return render(request, 'index.html')
def timeline(request):
    return render(request, 'timeline.html')
def works(request):
    return render(request, 'works.html')
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})
def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})
def search(request):
    return render(request, 'search.html')