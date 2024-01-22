from django.shortcuts import render, get_object_or_404, redirect
from .models import Avto
from django.contrib.auth.decorators import login_required
from .form import AvtoForm
from django.http import Http404, HttpResponseForbidden

def index(request):
    return render (request,'avto/index.html')

def avto_list(request):
    avtos = Avto.objects.filter(active= True)
    return render(request, 'avto/avto_list.html', {'avtos': avtos})

def avto_detail(request, avto_id):
    avto = get_object_or_404(Avto, id=avto_id)
    return render(request, 'avto/avto_detail.html', {'avto': avto})


@login_required
def new_avto(request):
    if request.method == 'POST':
        form = AvtoForm(request.POST , request.FILES)
        if form.is_valid():
            avto = form.save(commit=False)
            avto.author = request.user
            avto.save()
            return redirect('avto:user_avto')
    else:
        form = AvtoForm()
    
    return render(request, 'avto/new_avto.html', {'form': form})

@login_required
def user_avto(request):
    avtos = Avto.objects.filter(author = request.user)
    context = {"avtos": avtos}
    return render(request,'avto/user_avto.html', context )


@login_required
def edit_avto(request):
    avtos = Avto.objects.filter(author = request.user)
    context = {"avtos": avtos}
    return render(request,'avto/user_avto.html', context )

@login_required
def edit_avto(request, avto_id):
    avto = get_object_or_404(Avto, id=avto_id)
    if avto.author != request.user:
        raise Http404
    if request.method == 'POST':
        form = AvtoForm(request.POST, request.FILES, instance=avto)
        if form.is_valid():
            avto = form.save(commit=False)
            avto.author = request.user
            avto.save()
            return redirect('avto:user_avto')
    else:
        form = AvtoForm(instance=avto)
    
    return render(request, 'avto/edit_avto.html', {'form': form})

@login_required
def delete_avto(request, avto_id):
    avto = get_object_or_404(Avto, id=avto_id)

    if avto.author != request.user:
        return HttpResponseForbidden("У вас нет прав для удаления этого объявления.")

    if request.method == "POST":
        avto.delete()
        return redirect("avto:user_avto")

    context = {"avto": avto}
    return render(request, 'avto/delete_avto.html', context)