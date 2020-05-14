from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import *
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    request.session['name']='Username'
    request.session['password']='password'
    return HttpResponse("Hello you are loged in start creating your website from here")



def acccess_sess(request):
    response ="<h1> wel come to the session page </h1>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        response += '<p><a href = "/delete_sess" > delte session </a>'
        return HttpResponse(response)
    else:
        return redirect(index)

def delete_sess(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("session delete")


def Signup(request):

    form = SignUpForm()
    context = {
        'form': form,
        'name': 'signup'
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')


    return render(request,'form_signup.html',context)


def account_activation_sent(request):
    return HttpResponse("we have sent you an email")

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.profile.email_confirmed = True
        user.save()
        login(request,user)
        return redirect(acccess_sess)
    else:
        return render(request,'account_activation_invalid.html')



def user_log(request):

    form=user_loginform()
    context={
        'form' : form,
        'name': 'login'
    }

    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None and user.is_active == True:
            login(request,user)
            return HttpResponse("userogin")
        else:
            try:
                user_exist=User.objects.get(username=username)
                email_conf=Profile.objects.get(user=user_exist)
                if email_conf.email_confirmed == False:
                    sam=user_exist.email
                    messages.error(request,"The email "+sam+ " is not verified")
                else:
                    messages.error(request,"The password is wrong")
            except:
                messages.error(request,"invalid email")



    return render(request,'form_signup.html',context)


def password_reset(request):
    return HttpResponse("its to de done")

def uname(request):
    pro=User.objects.all()
    print(pro)

    return HttpResponse("<h1>somy</h1>")