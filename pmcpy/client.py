import urllib.request
import json


class client:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.auth_token = ''


    @staticmethod
    def request(method, url, headers, body=""):
        if body == "":
            request = urllib.request.Request(url, headers=headers)
        else:
            request = urllib.request.Request(
                url, json.dumps(body).encode("utf-8"), headers=headers)
        request.get_method = lambda: method
        response = urllib.request.urlopen(request)
        response_string = response.read().decode('utf-8')
        response_code = response.getcode()
        if not 200 <= response_code <= 299:
            print("Request to", response.geturl(),
                  "failed. Error details:", response_string)
        if response_string:
            return json.loads(response_string)
        else:
            return True


    from .auth import login
    from .apikey import (post_apikey,
                          put_apikey,
                          get_apikey,
                          delete_apikey)
    from .credentials import (list_credentials,
                              post_credentials,
                              disable_credential,
                              update_credential,
                              delete_credential,
                              get_example_aws_policy,
                              get_example_azure_policy,
                              get_credential_ingestion,
                              start_credential_ingestion)
    from .resource import (attach_schedule,
                           cancel_override_schedule,
                           detach_schedule,
                           get_parking_compatible_types,
                           get_parking_configuration,
                           get_parking_restriction,
                           get_resource,
                           override_schedule,
                           put_parking_configuration,
                           put_parking_restriction,
                           put_resize_recommendation_flag,
                           put_smartpark_recommendation_flag,
                           resize_compatible_types,
                           resize_custom_types,
                           resize_instance_type,
                           set_cost,
                           list_resources
                           )
    from .resource_v1 import (change_resources_team_v1,
                              get_resource_details_v1,
                              get_resource_states_v1,
                              get_resource_stats_v1,
                              get_resources_v1,
                              list_resources_v1,
                              toggle_resources_v1
                              )
