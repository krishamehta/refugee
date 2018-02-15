from django.shortcuts import render, redirect
from .forms import Register, ProfileInfo
from django.contrib.auth import authenticate, login
'''
from .models import Benefactor
from book_listing.models import Book_List
from forum.models import Post
'''


def home(request):
    return render(request, 'registration/home.html')


def menu(request):
    return render(request, 'registration/menu.html')


def donorPage(request):
    return render(request, 'registration/donorPage.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Register(request.POST)
        profile_form = ProfileInfo(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            login(request, authenticate(username=username, password=raw_password))
            registered = True
    else:
        user_form = Register(request.POST)
        profile_form = ProfileInfo(request.POST, request.FILES)
    if registered:
        return redirect('/booklisting/search/')
    else:
        return render(request, 'sign_in/register.html', {'user_form': user_form, 'profile_form': profile_form})


'''
def profile(request):
    user = Profile.objects.get(user=request.user)
    books = Book_List.objects.filter(user=request.user)
    post = Post.objects.filter(user=request.user)
    return render(request, 'sign_in/profile.html', {'user': user, 'books': books, 'forum': post})
'''
