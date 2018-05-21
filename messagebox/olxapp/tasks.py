import datetime

from django.conf import settings

from olxapp.clients import OLXAPIClient
from olxapp.models import Conversation, Message


def convert_date(data_str):
    return datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')


# TODO: podpiąć w Celery lub zrobić prosty przycisk refresh na głównej stronie

def update_conversations():
    olx_api_client = OLXAPIClient(
        client_id=settings.OLX_CLIENT_ID,
        client_secret=settings.OLX_CLIENT_SECRET,
        password=settings.OLX_PASSWORD,
        username=settings.OLX_USERNAME,
    )
    for conversation_data in olx_api_client.get_conversations():
        conversation, _ = Conversation.objects.get_or_create(
            external_id=conversation_data['id'],
            defaults={
                'created_at': convert_date(conversation_data['created_at'])
            }
        )
        for message_data in olx_api_client.get_messages(conversation_data['id']):
            Message.objects.get_or_create(
                external_id=message_data['id'],
                defaults={
                    'created_at': convert_date(message_data['created_at']),
                    'conversation': conversation,
                    'message': message_data['message'],
                }
            )
