from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Reply
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user=get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

# class PostDetailView(DetailView):
#     model = Post

def make_reply(toreply):
    jist = []
    new_reply = Reply.objects.all().filter(to_reply=toreply)

    for new in new_reply:
        jist = jist + [new]
        jist = jist + make_reply(new.id)

    return jist

def postDetailView(request, pk):
    object = Post.objects.get(pk=pk)
    toreply,created = Reply.objects.get_or_create(message="Type your reply..", postId=object.id)
    reply_list = []
    reply_list += [toreply]
    reply_list += make_reply(toreply.id)

    return render(request, 'blog/post_detail.html', {'object':object, 'reply_list':reply_list})

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','text']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','text']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

@login_required
def postDeleteView(request, pk):
    post = Post.objects.get(pk=pk)
    if post.author == request.user:
        reply = Reply.objects.get(postId=post.id)
        delete_func(reply.pk)
        reply.delete()
        post.delete()
    return redirect('blog-home')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def reply(request, pk, v):
    if request.method == 'POST':
        form_data = request.POST['message']

        left_margin = Reply.objects.get(pk=pk).left_margin + 20

        if pk % 10 == 0:
            color_field = "w3-metro-green"
        elif pk % 10 == 1:
            color_field = "w3-metro-blue"
        elif pk % 10 == 2:
            color_field = "w3-metro-magenta"
        elif pk % 10 == 3:
            color_field = "w3-flat-sun-flower"
        elif pk % 10 == 4:
            color_field = "w3-flat-emerald"
        elif pk % 10 == 5:
            color_field = "w3-flat-belize-hole"
        elif pk % 10 == 6:
            color_field = "w3-flat-amethyst"
        elif pk % 10 == 7:
            color_field = "w3-metro-light-purple"
        elif pk % 10 == 8:
            color_field = "w3-flat-pumpkin"
        elif pk % 10 == 9:
            color_field = "w3-flat-orange"

        Reply.objects.create(to_reply=pk, message=form_data, left_margin=left_margin, color_style=color_field)
    return redirect('post-detail',pk=v)

def delete_func(pk):
    vist = Reply.objects.all().filter(to_reply=pk)
    for reply in vist:
        delete_func(reply.pk)
        reply.delete()

def delete_reply(request, pk, v):
    reply = Reply.objects.get(pk=pk)
    delete_func(reply.pk)
    reply.delete()
    return redirect('post-detail',pk=v)
