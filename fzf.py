from math import ceil
import json
from pprint import pprint

from concurrent.futures import ThreadPoolExecutor, as_completed

from iterfzf import iterfzf

from pmcpy import client


creds = json.loads(open(".pmc", 'r').read())
c = client("https://awsgov.parkmycloud.com")

c.login(**creds)

raw_items = {}

def stringify(item):
    global raw_items
    raw_items[item['id']] = item
    trimmed_item = {key: item[key] for key in ('cred_name', 'name', 'state', 'info', 'team_name', 'id')}
    return json.dumps(trimmed_item)


def iter_items():
    response = c.list_resources(pageSize=100)
    for item in response['items']:
        yield stringify(item)
    limit, total = response['limit'], response['total']

    with ThreadPoolExecutor(max_workers=10) as thread_pool:
        futures  = [thread_pool.submit(c.list_resources, pageSize=100, page=page)
                    for page in range(1, ceil(total/limit)+1)]

        for future in as_completed(futures):
            for item in future.result()['items']:
                yield stringify(item)


#[pprint(raw_items[json.loads(x)['id']]) for x in iterfzf(iter_items(), multi=True, exact=True)]





#pprint(c.get_resource_details_v1(resource_id))

# pprint(c.override_schedule([resource_id], override_period=4))

# pprint(c.toggle_resources_v1([resource_id], action='start'))
