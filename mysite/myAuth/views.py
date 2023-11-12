from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


from .forms import LoginForm, RegisterForm, GuestForm
from .token import account_activation_code
from .models import GuestEmail
from django.contrib.auth.tokens import default_token_generator



def activate(request, uidb64, token):
    return redirect('/myAuth/login_page/')

def activationEmail(request, user, to_email):
    mail_subject = "Activate your account here!!"
    message = render_to_string("account_activation.html", {
        'user' : user.full_name,
        'domain': get_current_site(request).domain,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : account_activation_code.make_token(user),
        "protocol" : 'https' if request.is_secure() else 'http'

    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request,f'Dear <b>{user}<b/>, please go to your email<b>{to_email}</b> inbox and activate your account <b> Note</b> If you do not see you can check your spam')
    else:
        messages.error(request,f'Please you can check your email {to_email}')





def Index(request):
    return render(request, "index.html")


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email       = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

def logout_page(request):
    logout(request)
    return redirect('/')



def login_page(request):
    return render(request, "myAuth/login.html")


def login_api(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                print("user no come")
                return redirect("/myAuth/login_page/" )
        else:
            print("validation no come")
            return redirect("/myAuth/login_page/" )
    else: 
        print("Post no come")
        return redirect("/myAuth/login_page/", )



# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username  = form.cleaned_data.get("username")
#         password  = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
            
#                 return redirect("/")
#         else:
#             # Return an 'invalid login' error message.
#             print("Error")
#     return render(request, "myAuth/login.html", context)


User = get_user_model()
def register(request):
    return render(request, "myAuth/register.html")

def register_api(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()   
            activationEmail(request, user, form.cleaned_data.get('email'))         
            return redirect("/")
            messages.success("Please Check your email for confirmation")

        else:
            print("form not valid")
            return redirect("/myAuth/register")
    else:
        print("post request not valid")
        return redirect("/myAuth/register")


