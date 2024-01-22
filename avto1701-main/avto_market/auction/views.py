from django.shortcuts import render, redirect , get_object_or_404
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import AuctionForm , BuyerForm, CommentForm
from .models import Auction, Buyer, Comment
from avto.models import Avto 
from django.contrib.auth.models import User
from account.models import Message, Profile
from django.urls import reverse
from django.core.mail import send_mail

@login_required
def auction_create(request, avto_id):
    avto = get_object_or_404(Avto, id=avto_id)
    if avto.author != request.user:
        return HttpResponseForbidden("У вас нет прав для удаления этого объявления.")
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.avto = avto
            auction.save()
            return redirect('avto:user_avto')
    else:
        form = AuctionForm()
    
    return render(request, 'auction/auction_create.html', {'form': form})

def view_all_auctions(request):
    auctions = Auction.objects.filter(active=True) 
    buyers = Buyer.objects.all()
    return render(request, 'auction/view_all_auctions.html', {'auctions': auctions, 'buyers': buyers})


@login_required
def view_user_auctions(request):
    user = request.user
    auctions = Auction.objects.filter(avto__author=user)  
    context = {
        'auctions': auctions
    }   
    return render(request, 'auction/view_user_auctions.html', context)


@login_required
def edit_auction(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)

    if auction.avto.author != request.user and not request.user.is_superuser:
        raise Http404

    if request.method == 'POST':
        form = AuctionForm(request.POST, instance=auction)

        if form.is_valid():
            form.save()
            return redirect('auction:view_user_auctions',)
    else:
        form = AuctionForm(instance=auction)

    context = {
        'form': form,
        'auction': auction
    }

    return render(request, 'auction/edit_auction.html', context)


@login_required
def create_buyer(request, auction_id, user_id):
    auction = get_object_or_404(Auction, id=auction_id)
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.auction = auction
            buyer.user = user
            if buyer.last_bid_price < auction.start_price:
                form.add_error('last_bid_price', 'Стартовая цена не может быть меньше цены предложения.')
            else:
                buyer.save()
                return redirect('auction:view_all_auctions')
    else:
        form = BuyerForm()

    return render(request, 'auction/create_buyer.html', {'form': form, 'auction': auction, 'user': user})


@login_required
def comment_create(request, auction_id, user_id):
    auction = get_object_or_404(Auction, id=auction_id)
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auction = auction
            comment.author = user
            comment.save()
            return redirect('auction:auction_detail', auction_id=auction_id)
    else:
        form = CommentForm()

    return render(request, 'auction/comment_create.html', {'form': form, 'auction': auction, 'user': user})

@login_required
def auction_detail(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    avto = auction.avto
    buyers = Buyer.objects.filter(auction=auction)
    comments = Comment.objects.filter(auction=auction)

    return render(request, 'auction/auction_detail.html', {'avto': avto, 'auction': auction, 'buyers': buyers, 'comments': comments,})


def winner(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    bidders = Buyer.objects.filter(auction=auction).order_by('-last_bid_price')

    if bidders:
        winner = bidders[0].user
    else:
        return render(request, 'auction/no_bidders.html')
        
    auction.active = False
    auction.save()
    admin = User.objects.get(username='admin')
    auction_detail_url = reverse('auction:auction_detail', args=[auction.id])
    absolute_url = request.build_absolute_uri(auction_detail_url)    
    message = Message(sender=admin , recipient= winner, text=f"Вы победили в аукционе - {auction.avto} -{auction.avto.model}, ниже ссылка на выйгранный аукцион", link=absolute_url)
    message.save()

    subject = 'Поздравляем с победой на аукционе'
    message_text = f"Вы победили в аукционе {auction.avto} - {auction.avto.model}. Ниже ссылка на выигранный аукцион:\n{absolute_url}"
    email_from = 'seva2411@yandex.ru'
    recipient_list = [winner.email]
    send_mail(subject, message_text, email_from, recipient_list)



    context = {
        'auction': auction,
        'bidders': bidders,
        'winner': winner
    }

    return render(request, 'auction/winner.html', context)



def profile_win(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)