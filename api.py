from datetime import datetime
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import LegacyApplicationClient


class CybApi:
    _base_url = "https://in.cyb.no/"

    def __init__(self, username, password, client_id, client_secret):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

        # Get a token via the Resource Owner Password Credential Grant OAuth2 API
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
        self._token = oauth.fetch_token(
                verify=False,
                token_url=self._base_url + "o/token/",
                username=username, password=password,
                client_id=client_id, client_secret=client_secret
                )
        # Make a client for connecting to the API.
        self._client = OAuth2Session(
                client_id,
                token=self._token,
                auto_refresh_url=self._base_url + "o/token/",
                auto_refresh_kwargs={
                    "client_id": client_id,
                    "client_secret": client_secret
                    },
                token_updater=self._token_updater
                )

    def _token_updater(self, token):
        self._token = token


    def get_members(self):
        url = self._base_url + 'api/member/members'
        response = self._client.get(url)

        if response.status_code != 200:
            raise Exception('%s: %s' % (response.status_code, response.text))

        return response.json()
