from django.shortcuts import render,redirect
from django.http import HttpResponse    
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.






def index(request):
     if request.user.is_anonymous:
      
        return redirect('/loginn')

     return render(request, 'index.html')



def admin1(request):
    return render(request, 'admin1.html')

def courses(request):
     if request.user.is_anonymous:
      
        return redirect('/loginn')
   

     return render(request, 'courses.html')

def messages(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'messages.html')

def settings(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'settings.html')




def web(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'web.html')


def data(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'data.html')


def software(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'software.html')

def video(request):
    if request.user.is_anonymous:
      
        return redirect('/loginn')
    return render(request, 'video.html')
    
def loginn(request):
     if request.method == 'POST':
        # superuser=request.user.is_superuser.POST["username"]
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # Superuser = authenticate(request, username=superuser, password=password)
        # if superuser is not None:
        #     login(request,superuser)
        #     return redirect("/admin1")

        if user is not None:
            login(request, user)
            return redirect('/')
        else: 
            return render(request, 'loginn.html')

     return render(request, 'loginn.html')

def logoutt(request):
    logout(request)
    return redirect('/loginn')


@login_required
def changepass(request):
    if request.method == 'POST':
       
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Updating the user's session
            update_session_auth_hash(request, user)
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('/loginn')  # Replace 'home' with the URL name of your home page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepass.html', {'form': form})
