def get_resources_v1(self, resource_id):
    url = self.endpoint + f"/eng/resources/{resource_id}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def get_resource_stats_v1(
        self,
        credential: str=None,
        location: str=None,
        metrics: bool=None,
        name: str=None,
        provider: str=None,
        recommended: bool=None,
        recommendation=None,
        schedule: str=None,
        search: str=None,
        state: str=None,
        status: str=None,
        tags: str=None,
        team: str=None,
        type=None):

    if not (location and name):
        raise ValueError("Both location and name must be provided!")

    bool_args_keys = {"name", "recommmended"}
    args_keys = {
        "credential",
        "location",
        "metrics",
        "name",
        "provider",
        "recommended",
        "recommendation",
        "schedule",
        "search",
        "state",
        "status",
        "tags",
        "team",
        "type"
    }

    args = []
    for k, v in locals().items():
        if k in args_keys:
            if k in bool_args_keys and not v:
                continue
            if v is not None:
                args.append(f"{k}={v}")

    url = self.endpoint + "/resources/stats"

    if args:
        url += "?" + "&".join(args)

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def list_resources_v1(
        self,
        credential: str=None,
        location: str=None,
        metrics: bool=None,
        name: str=None,
        provider: str=None,
        recommended: bool=None,
        recommendation=None,
        schedule: str=None,
        search: str=None,
        state: str=None,
        status: str=None,
        tags: str=None,
        team: str=None,
        type=None,
        page: int=None,
        pageSize: int=None,
        sort: str=None):

    if not (location and name):
        raise ValueError("Both location and name must be provided!")

    bool_args_keys = {"name", "recommmended"}
    args_keys = {
        "credential",
        "location",
        "metrics",
        "name",
        "provider",
        "recommended",
        "recommendation",
        "schedule",
        "search",
        "state",
        "status",
        "tags",
        "team",
        "type",
        "page",
        "pageSize",
        "sort"
    }

    args = []
    for k, v in locals().items():
        if k in args_keys:
            if k in bool_args_keys and not v:
                continue
            if v is not None:
                args.append(f"{k}={v}")

    url = self.endpoint + "/resources/paged"
    if args:
        url += "?" + "&".join(args)
    print(url)

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def get_resource_states_v1(self):
    url = self.endpoint + "/resource-states"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def toggle_resources_v1(self, item_ids, action: str=None):
    url = self.endpoint + "/resources/toggle"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    body = {
        "item_ids": item_ids,
    }
    if action is not None:
        body['action'] = action
    response = self.request("PUT", url, headers, body)

    return response


def change_resources_team_v1(self, item_ids, team_id):
    url = self.endpoint + "/resources/change-team"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    body = {
        "item_ids": item_ids,
        "team_id": team_id
    }

    response = self.request("PUT", url, headers, body)

    return response


def get_resource_details_v1(self, resource_id):
    url = self.endpoint + f"/resources/detail/{resource_id}"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response
