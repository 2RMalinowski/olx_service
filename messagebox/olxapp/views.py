from django.shortcuts import render
from olxapp.models import Conversation


def conversations_list_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'send':
            pass
        elif request.POST['action'] == 'refresh':
            pass
        conversations = Conversation.objects.all()
        return render(
            request=request,
            template_name='conversations_list.html',
            context={'conversations': conversations,
                     }
        )
