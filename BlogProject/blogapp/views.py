from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .forms import Create_Blog_Form,Create_Comment_Form
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog_Model,Comment,Like
# Create your views here.

def blog_home(request):
    all_blogs = Blog_Model.objects.all()
    context = {'all_blogs':all_blogs}
    return render(request,'blogapp/blog_home.html',context)


@login_required(login_url='loginapp:login')
def Create_Blog(request):
    form = Create_Blog_Form()
    if request.method == 'POST':
        form = Create_Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.save()
            return HttpResponse('YOUR BLOG IS SUCCESSFULLY MADE!')
        
    dict = {'form':form}
    return render(request,'blogapp/create_blog.html',dict)

class Edit_Blog(LoginRequiredMixin,UpdateView):
    model = Blog_Model
    fields = ('title','image','description','category')
    template_name = ('blogapp/edit_blog.html')

    def get_success_url(self):
        return reverse_lazy('loginapp:user_profile')


class Delete_Blog(LoginRequiredMixin,DeleteView):
    model = Blog_Model
    template_name = ('blogapp/delete_blog.html')

    def get_success_url(self):
        return reverse_lazy('loginapp:user_profile')
    
def Blog_Details(request,pk):
    blog_model = Blog_Model.objects.get(pk=pk)
    form = Create_Comment_Form()
    current_user = request.user
    comments = Comment.objects.filter(blog=blog_model)
    if current_user.is_authenticated:

        if request.method == 'POST':
            form = Create_Comment_Form(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.user = request.user
                form_instance.blog = blog_model
                form_instance.save()
                return HttpResponse('Congratulations! Your Comment Is Published!')
        dict = {'form':form,'blog_model':blog_model,'comments':comments}
        return render(request,'blogapp/blog_details.html',dict)
    else:
        dict = {'blog_model':blog_model,'comments':comments}
        return render(request,'blogapp/blog_details.html',dict)
    


@login_required
def like_blog(request,pk):
    blog_model = Blog_Model.objects.get(pk=pk)
    like = Like.objects.filter(user=request.user,blog=blog_model).first()
    if like:
        like.delete()
        has_liked = False
    else:
        Like.objects.create(user=request.user,blog=blog_model)
        has_liked = True
    liked_count = Like.objects.filter(blog=blog_model).count()
    context= {'has_liked':has_liked,'blog_model':blog_model,'liked_count':liked_count}
    return render(request,'blogapp/blog_details.html',context)
