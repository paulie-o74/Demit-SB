from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import CommentForm, PostForm




class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment is awaiting approval, thank you for sharing.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


@login_required
def add_post(request):
    """ Add a post to the journal """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html',
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit a post in the journal """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
    