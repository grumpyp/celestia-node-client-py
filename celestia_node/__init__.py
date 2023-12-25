import os
import requests
from loguru import logger

from .blob import Blob


class Client:
    """
    Base class for the API connection to handle requests.
    Saves the API URL and the API key.
    """

    @logger.catch(reraise=True)
    def __init__(self, url: str = None, api_key: str = None, log=False) -> None:
        self.url = url if url else "http://127.0.0.1:26658"
        self.api_key = api_key if api_key else os.environ.get('CELESTIA_NODE_AUTH_TOKEN')
        self.log = log

        # Please attach Logs to any issue opened on GitHub
        if self.log is True:
            logger.add("log.log", level="TRACE", rotation="100 MB")

        if self.api_key is None:
            raise KeyError(
                "No API key found. Please set the CELESTIA_NODE_AUTH_TOKEN environment variable or pass it as an"
                " argument to the Client class.")

    def request(self, payload, print_response=True) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        r = requests.post(self.url, headers=headers, json=payload)

        if print_response:
            print(r.json())

        if 'error' in r.json().keys():
            if self.log is True:
                logger.log('CRITICAL', f"Error in the Node request {r.json()['error']}")
            return r.json()

        return r.json()["result"]
