from django.shortcuts import render
from posts.models import Post
#from django.shortcuts import HttpResponse
# Create your views

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':

        #products = Post.objects.all()

        #context = {
            #'products': products
        #}
        return render(request, 'products/products.html')#,context=context)