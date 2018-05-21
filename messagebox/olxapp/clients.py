import requests


class OLXAPIClient:
    OLX_API_URL = 'https://www.olx.pl/api/open'

    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
    
    def get_conversations(self):
        response = requests.get(
            url=self.OLX_API_URL + '/account/me/conversations/all',
            headers={'Authorization': 'Bearer ' + self._get_access_token()}
        )
        return response.json()['results']

    def get_messages(self, conversation_id):
        response = requests.get(
            url=self.OLX_API_URL + f'/conversations/{conversation_id}/messages',
            headers={'Authorization': 'Bearer ' + self._get_access_token()}
        )
        return response.json()['results']

    # TODO: do zaimplementowania wysyłanie wiadomości
    # def send_message(self, conversation_id, message_content):
    #     ...

    def _get_access_token(self):
        response = requests.post(
            url=self.OLX_API_URL + '/oauth/token',
            data={
                "grant_type": "password",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "password": self.password,
                "username": self.username,
                "scope": "read write",
            }
        )
        return response.json()['access_token']

