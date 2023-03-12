from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .forms import Create_Blog_Form
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog_Model
# Create your views here.
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
    
class Blog_Details(DetailView):
    model = Blog_Model
    template_name = ('blogapp/blog_details.html')