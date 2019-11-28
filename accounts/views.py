from django.contrib import messages
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from . forms import SignUpForm
from . tokens import account_activation_token
from posts.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            
            subject = 'Aktivasi akun rupher'
            message = render_to_string('activation_email.html',{
                'user' : user,
                'domain' : get_current_site(request).domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user) 
            })

            user.email_user(subject,'',html_message=message)
            messages.success(request,'silahkan cek inbox email anda')
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html',{'form':form})


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64).decode())
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_validated = True
        user.save()

        login(request, user)
        messages.success(request,'berhasil aktivasi')
        return redirect('home')
    else:
        messages.success(request,'kesalahan aktivasi')
        return redirect(reverse('login'))

@login_required
def edit_user(request):
    user = User.objects.get(pk=request.user.id)
    errors = []
    domain = get_current_site(request).domain

    if request.method == "POST" and request.FILES['image']:
        file = request.FILES['image']
        allow_ext = ['image/jpeg','image/png']
        
        
        if file.size < 2097152:
            if file.content_type in allow_ext:
                newfilename = get_random_string(length=18, allowed_chars='1234567890') + '.jpg'
                fs  = FileSystemStorage(location='storage/image_profile')
                fs.save(newfilename, file)
                user.profile.user_image = newfilename
                user.profile.save()
                return HttpResponseRedirect('/dashboard')
            else:
                errors.append('ekstentesi tidak didukung')
        else:
            errors.append('ukuran file terlalu besar')

    
    return render(request,'settings.html',{'user':user,'errors':errors,'domain':domain})


