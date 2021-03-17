# from dataclasses import dataclass
from datetime import datetime

# from .client import client
# from .data_structures import data_structure

from dateutil import parser


def login(self, key, key_id, duration=43200):
    auth_url = self.endpoint + "/v2/auth/login"

    headers = {
        "Content-Type": "application/json",
    }

    # Get the access token from ParkMyCloud
    # This token is used to access other APIs
    login_codes = {
        'key': key,
        'key_id': key_id,
        'duration': duration
    }

    auth_dict = self.request("POST", auth_url, headers, login_codes)

    self.auth_token = auth_dict['token']
    self.expiration_time = datetime.fromisoformat(auth_dict['expiration_time'][:26])
    return {"auth_token": self.auth_token,
            "expiration_time": self.expiration_time}
