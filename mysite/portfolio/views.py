from django.shortcuts import render
from blog.models import Post

def portfolio_home(request):
    # Obtener los últimos 2 posts para mostrar en el portfolio
    recent_posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')[:2]
    return render(request, 'portfolio/index.html', {'recent_posts': recent_posts})