=================
django-mynewsdesk
=================

Django package for MyNewsDesk API

Installation
------------

Use your favorite Python installer to install it from PyPI::

    pip install django-mynewsdesk

Quick start
-----------

1. Add "mynewsdesk" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mynewsdesk',
    )

2. Add MYNEWSDESK_KEY to settings like this::

    MYNEWSDESK_KEY = 'your unique key'

3. For South support, customize the SOUTH_MIGRATION_MODULES setting like so::

    SOUTH_MIGRATION_MODULES = {
        'mynewsdesk': 'mynewsdesk.south_migrations',
    }

4. Run `python manage.py migrate` to create the polls models.


API
---

- mynewsdesk.api.request(service, params) - request to MyNewsDesk API

    service: MyNewsDesk API service name
    params: params for request

    return: request response (request library)


- mynewsdesk.api.get_list(type_of_media) - request material list

    type_of_media: mynewsdesk.models.TYPE_PRESSRELEASE, mynewsdesk.models.TYPE_NEWS, etc...

    returns: JSON from api request


- mynewsdesk.api.subscribe(email, types_list) - subscribe email

    email: e-mail of subscriber
    types_list: list of material types for subscription


- mynewsdesk.sync.sync_list(type_of_media) - synchronize materials to local database

    type_of_media: mynewsdesk.models.TYPE_PRESSRELEASE, mynewsdesk.models.TYPE_NEWS, etc...

    returns: dictionary like this {updated: n, create: n, errors: n}


- mynewsdesk.sync.sync_all() - synchronize materials of all types to local database

    returns: dictionary like this {updated: n, create: n, errors: n}


Contribute & Support
--------------------

If you have an issue requests, or you find a bug, you can easily report them on GitHub Issues.
If you want to fix bug or create new feature, just fork, make changes and create a pull request. List of TODOs you can find below here.
Furthermore, you can create better documentation.

TODO
----

- method for 'view' API service
- method for 'search' API service
- method for 'pressroom_info' API service
- method for 'create_comment' API service
- uncomment models and parse 'subjects'
- uncomment models and parse 'geographic_areas'
- uncomment models and parse 'contact_peoples'
- uncomment models and parse 'comments'
- parse 'related_items'
- parse 'instant_messaging'

Credits
-------

Created and maintained by `Pavel Kozlov <http://pkozlov.ru/>`_