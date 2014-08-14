from django.conf import settings
import requests
from mynewsdesk import models


def request(service, params={}):
    url = 'http://www.mynewsdesk.com/services/pressroom/' + service + '/' + settings.MYNEWSDESK_KEY + '/'
    return requests.get(url, params=params)


def json_request(service, params={}):
    params['format'] = 'json'
    r = request(service, params)
    return r.json()


def get_list(type_of_media=models.TYPE_PRESSRELEASE, limit=20, offset=0, order=False, callback=False, pressroom=False, archived=False):
    params = {
        'type_of_media': type_of_media,
        'limit': limit,
        'offset': offset
    }

    if pressroom:
        params['pressroom'] = pressroom

    if order:
        params['order'] = order

    if archived:
        params['archived'] = 'true'

    if callback:
        params['callback'] = callback

    return json_request('list', params)

def subscribe(email, types_list):
    params = {
        'newsdesk_subscriber_email': email
    }
    for stype in types_list:
        params['newsdesk_subscribe_to_' + models.SUBSCRIBE_ENDINGS[stype]] = 1
    r = request('subscribe', params)
    if r.status_code == requests.codes.ok:
        return True
    else:
        return False

# TODO: method for 'view' service
# TODO: method for 'search' service
# TODO: method for 'pressroom_info' service
# TODO: method for 'create_comment' service