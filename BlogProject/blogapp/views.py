from django.shortcuts import render,HttpResponse
from .forms import Create_Blog_Form
from django.contrib.auth.decorators import login_required
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