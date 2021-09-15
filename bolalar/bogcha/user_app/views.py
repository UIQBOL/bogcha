from .models import Customer
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from .decorators import *
from .forms import UserForm, User, CustomerForm
from django.contrib.auth.decorators import login_required



# class SignUpView(CreateView):
#     form_class=UserForm
#     success_url='/login'
#     template_name='user_app/registration.html'

# Create your views here.
@allowed_users(allowed_users=['admin1'])
def userRegistartion(request):

    userform = UserForm()
    if request.method == 'POST':
        userform =UserForm(data=request.POST)
        if userform.is_valid():
            formdata = userform.cleaned_data
            del formdata["confirm"]

            currentuser = User(**formdata)
            print(currentuser)
            print("------------------------------------")
            print(userform)
            currentuser.set_password(formdata['password'])
            currentuser.save()

            Customer.objects.create(user=currentuser, name=userform.cleaned_data["username"])

            messages.success(request, 'User created successfully!!!')
            return redirect('userLogin')

    context = {'form': userform}
    return render(request, 'user_app/registration.html', context)


@unauthenticated_user
def userLogin(request):
    if request.user.is_authenticated:
        return render('blog')
    else:
        
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.success(request, 'Error...')
        return render(request, 'user_app/login.html')


def userLogout(request):
    logout(request)
    return redirect('userLogin')


def userProfile(request):


    return render(request, 'user_app/userprofile.html')


def editprofile(request):
    user=request.user.customer
    myform=CustomerForm(instance=user)


    if request.method=='POST':
        form=CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    
    context={'myform':myform}
    return render(request, 'user_app/editprofile.html', context)
