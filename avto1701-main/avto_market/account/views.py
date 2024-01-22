from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  UserRegistrationForm, ProfileEditForm, MessageForm
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Profile , Message
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)


def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'account/edit_profile.html', context)

@login_required
def messages_view(request):
    user = request.user
    messages = Message.objects.filter(sender=user) | Message.objects.filter(recipient=user)
    messages = messages.order_by('-created_at') 
    return render(request, 'account/messages_view.html', {'messages': messages})


@login_required
def messages_detail(request, messages_id):
    message = Message.objects.get(id=messages_id)
    if message.sender != request.user and message.recipient != request.user:
        return HttpResponseForbidden("У вас нет прав для чтения этого сообщения.")
    
    context = {'message': message}
    return render(request, 'account/messages_detail.html', context)

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  
            message.save()
            return redirect('account:messages_view')  
    else:
        form = MessageForm()

    return render(request, 'account/send_message.html', { 'form': form })


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']

        user = authenticate(username=request.user.username, password=current_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            return redirect('account:password_change_done') 

    return render(request, 'account/change_password.html')


def password_change_done(request):
    return render (request,'account/password_change_done.html')


