from django.shortcuts import render, redirect
from posts.models import Post, Review
from posts.forms import PostCreateForm, ReviewCreateForm
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


def post_detail_view(request,id):

    if request.method == 'GET':
        post = Post.objects.get(id=id)
        #reviews = Review.objects.filter(post_id=id)
        context = {

            'post': post,
            'reviews': post.review_set.all(),
            'form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=context)


    if request.method == 'POST':
        post = Post.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                post_id=id
            )
        context = {
            'post': post,
            'reviews': post.review_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)
def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                image=form.cleaned_data.get('image')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
