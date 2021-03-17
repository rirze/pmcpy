from datetime import datetime


def parse_date_to_string(obj, utc=False):
    if isinstance(obj, datetime):
        if not utc:
            return datetime.isoformat(obj)
        else:
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        return str(obj)
