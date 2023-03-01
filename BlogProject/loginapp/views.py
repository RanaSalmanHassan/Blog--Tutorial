from django.contrib.auth import login,authenticate
from .forms import SignUpForm,Edit_Profile_Form
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Signed Up Successfully!')

    dict = {'form': form}
    return render(request, 'loginapp/signup.html', dict)


def login_page(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponse('Logged In Successfully!')
                return HttpResponseRedirect(reverse('loginapp:user_profile'))
    dict = {'form': form}
    return render(request, 'loginapp/login.html', dict)

def user_profile(request):
    return render(request,'loginapp/profile.html')

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = Edit_Profile_Form(instance=current_user)
    if request.method == 'POST':
        form = Edit_Profile_Form(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            form = Edit_Profile_Form(instance=current_user)
            return HttpResponseRedirect(reverse('loginapp:user_profile'))
    dict = {'form':form}
    return render(request,'loginapp/edit_profile.html',dict)