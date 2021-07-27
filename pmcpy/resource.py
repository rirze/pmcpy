from .common_utils import parse_date_to_string

def get_resource(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def set_cost(self, resource_id, cost):
    url = self.endpoint + f"/v2/resource/{resource_id}/set_cost?cost={cost}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def reset_cost(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/reset_cost"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def resize_compatible_types(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/resize/compatible-types"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def resize_custom_types(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/resize/custom_limits"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def resize_instance_type(self, resource_id, instance_type):
    url = self.endpoint + f"/v2/resource/{resource_id}/resize/instance-type/{instance_type}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def get_parking_restriction(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/restriction"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def put_parking_restriction(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/restriction"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("PUT", url, headers)

    return response


def put_resize_recommendation_flag(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/resize-recommendations"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("PUT", url, headers)

    return response


def put_smartpark_recommendation_flag(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/smartpack-recommendations"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("PUT", url, headers)

    return response


def attach_schedule(self, item_ids, schedule_id):
    url = self.endpoint + "/v2/resource/attach-schedule"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body = {
        "items_ids": item_ids,
        "schedule_id": schedule_id
    }

    response = self.request("PUT", url, headers, body)

    return response


def detach_schedule(self, item_ids):
    url = self.endpoint + "/v2/resource/detach-schedule"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body = {
        "items_ids": item_ids,
    }

    response = self.request("PUT", url, headers, body)

    return response


def override_schedule(self, item_ids,
                      override_period=None,
                      override_until=None,
                      timezone=None):
    url = self.endpoint + "/v2/resource/override"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body = {
        "items_ids": item_ids,
    }
    if override_period:
        body["override_period"] = override_period
    if override_until:
        body["override_until"] = parse_date_to_string(override_until, utc=True)
    if timezone:
        body['timezone'] = timezone

    response = self.request("PUT", url, headers, body)

    return response


def cancel_override_schedule(self, item_ids):
    url = self.endpoint + "/v2/resource/override/cancel"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body = {
        "items_ids": item_ids,
    }

    response = self.request("PUT", url, headers, body)

    return response


def get_parking_configuration(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/parking/config"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def put_parking_configuration(self, resource_id, throttled_size, throttled_storage):
    url = self.endpoint + f"/v2/resource/{resource_id}/parking/config"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body = {
        "throttled_size": throttled_size,
        "throttled_storage": throttled_storage
    }

    response = self.request("PUT", url, headers, body)

    return response



def get_parking_compatible_types(self, resource_id):
    url = self.endpoint + f"/v2/resource/{resource_id}/parking/compatible_types"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response

def list_resources(
        self,
        order: str=None,
        location: str=None,
        metrics: bool=None,
        name: str=None,
        provider: str=None,
        schedule: str=None,
        search: str=None,
        state: str=None,
        tags: str=None,
        team: str=None,
        page: int=None,
        pageSize: int=None
):

    if page:
        if not pageSize:
            pageSize = 200
        page *= pageSize

    bool_args_keys = {"name", "recommmended"}
    args_keys      = {
        "credential"     : "cred_name",
        "location"       : None,
        "metrics"        : "has_heatmap_data",
        "name"           : None,
        "provider"       : None,
        "schedule"       : None,
        "search"         : None,
        "state"          : None,
        "tags"           : None,
        "team"           : None,
        "page"           : "offset",
        "pageSize"       : "limit",

    }

    args = []
    for k, v in locals().items():
        if k in args_keys:
            if k in bool_args_keys and not v:
                continue
            if v is not None:
                if arg_name:= args_keys[k]:
                    k = arg_name
                args.append(f"{k}={v}")

    url = self.endpoint + "/v2/resourcequery"
    if args:
        url += "?" + "&".join(args)

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response
