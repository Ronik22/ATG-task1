from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat


""" Chatroom between users """
@login_required
def room(request):
    chats = Chat.objects.all().order_by('date')
    context = {
        'old_chats':chats,
        'my_name':request.user,
    }
    return render(request, 'chat/chatroom.html', context)
