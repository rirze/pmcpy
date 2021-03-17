from dataclasses import dataclass

# from .client import client
from .data_structures import data_structure


def _generate_method(method):
    def function(self, apikey=''):
        url = self.endpoint + f"/v2/apikey/{apikey}"

        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': self.auth_token
        }
        response = self.request(method, url, headers)

        return response

    return function

post_apikey = _generate_method("POST")
put_apikey = _generate_method("PUT")
get_apikey = _generate_method("GET")
delete_apikey = _generate_method("DELETE")
