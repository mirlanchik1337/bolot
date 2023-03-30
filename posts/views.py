from django.shortcuts import render
from posts.models import Post, Review

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')
def products_view(request):
    if request.method == 'GET':

        posts = Post.objects.all()

        context = {
            'posts': posts
        }
        return render(request, 'products/products.html',context=context)


def post_detail_view(request, id):

    if request.method == 'GET':
        post = Post.objects.get(id=id)
        reviews = Review.objects.filter(post_id=id)
        context = {
            'post': post,
            'reviews': post.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)