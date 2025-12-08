from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Post

# CREATE
# def post_create(request):
#     if request.method == "POST":
#         company = request.POST.get("company")
#         title = request.POST.get("title")   
#         price = request.POST.get("price")
#         daraja = request.POST.get("daraja")
#         typework = request.POST.get("typework")
#         desc = request.POST.get("desc")
#         image = request.FILES.get("image")

#         Post.objects.create(
#             company=company,
#             title=title,
#             price=price,
#             daraja=daraja,
#             typework=typework,
#             desc=desc,
#             image=image
#         )
#         return redirect('post_list')

#     return render(request, "admin-add.html")
def home(request):
    q = request.GET.get("q", "")
    posts = Post.objects.filter(title__icontains=q) if q else Post.objects.all()

    return render(request, "index.html", {"posts": posts})
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "index.html", {'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post': post})




# # UPDATE
# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == "POST":
#         post.company = request.POST.get("company")
#         post.title = request.POST.get("title")
#         post.price = request.POST.get("price")
#         post.daraja = request.POST.get("daraja")
#         post.typework = request.POST.get("typework")
#         post.desc = request.POST.get("desc")
#         if request.FILES.get("image"):
#             post.image = request.FILES.get("image")
#         post.save()
#         return redirect('post_list')

#     return render(request, "post_update.html", {'post': post})

# # DELETE
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post_list')
