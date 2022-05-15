from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category,Coment
from .forms import PostForm, UpdateForm , ComentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail-articl', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_post']

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryListView(request):
    cat_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_lis': cat_list})


class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        coments = Coment.objects.all()
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cats_menu"] = cats_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["coments"] = coments
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddComent(CreateView):
    model = Coment
    form_class = ComentForm
    template_name = 'add_coment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        coments = Coment.objects.all()
        context = super(AddComent,self).get_context_data(**kwargs)
        context["coments"] = coments
        return context

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DelPost(DeleteView):
    model = Post
    template_name = 'deled.html'
    success_url = reverse_lazy('home')
