from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog.html')
    
def blog_posts(request):
    return render(request, 'blog_post.html')