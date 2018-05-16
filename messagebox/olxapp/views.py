from django.shortcuts import render
from olxapp.models import Conversation, Answer


def conversations_list_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'send':
            pass
        # TODO: wysłać wiadomość
        # 1. pobrać idki z request.POST.getlist('conversations')
        # 1. stworzyć OLXAPIClient
        # 2. wywołać olx_api_client.send_message
        elif request.POST['action'] == 'refresh':
            pass
        # TODO: odświeżyć wiadomości przy wykorzszytaniu update_conversations
        conversations = Conversation.objects.all()
        return render(
            request=request,
            template_name='conversations_list.html',
            context={'conversations': conversations,
                     }
        )


def answers_list(request):
    answers = Answer.objects.all
    return render(request, 'olxapp/answers_list.html', {'answers': answers})
