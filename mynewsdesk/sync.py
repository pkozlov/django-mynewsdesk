from mynewsdesk import models, api

def add_report(report, result):
    report['created'] += result['created']
    report['updated'] += result['updated']
    report['errors'] += result['errors']
    return report

def sync_all():
    report = {
        'created': 0,
        'updated': 0,
        'errors': 0
    }

    r = sync_list(models.TYPE_PRESSRELEASE)
    report = add_report(report, r)

    r = sync_list(models.TYPE_NEWS)
    report = add_report(report, r)

    r = sync_list(models.TYPE_BLOG_POST)
    report = add_report(report, r)

    r = sync_list(models.TYPE_CONTACT_PERSON)
    report = add_report(report, r)

    r = sync_list(models.TYPE_DOCUMENT)
    report = add_report(report, r)

    r = sync_list(models.TYPE_EVENT)
    report = add_report(report, r)

    r = sync_list(models.TYPE_IMAGE)
    report = add_report(report, r)

    r = sync_list(models.TYPE_VIDEO)
    report = add_report(report, r)

    return report

def add_link(material, link):
    db_link = models.Link(material=material, url=link['url'], text=link['text'])
    db_link.save()

def sync_list(service=models.TYPE_PRESSRELEASE):
    item_list = api.get_list(service)
    report = {
        'created': 0,
        'updated': 0,
        'errors': 0
    }
    if item_list and 'items' in item_list.keys() and 'item' in item_list['items']:
        for item in item_list['items']['item']:
            try:
                try:
                    db_item = models.Material.objects.get(id=item['id'])
                    report['updated'] += 1
                except models.Material.DoesNotExist:
                    db_item = models.Material(id=item['id'])
                    report['created'] += 1

                for key, val in item.items():
                    if not isinstance(val, list) and not (type(val) is dict):
                        setattr(db_item, key, val)

                db_item.save()

                for key, val in item.items():
                    if isinstance(val, list) or (type(val) is dict):
                        if 'channels' == key:
                            for channel in val['channel']:
                                try:
                                    db_channel = models.Channel.objects.get(id=channel['id'])
                                except:
                                    db_channel = models.Channel(id=channel['id'], title=channel['text'])
                                    db_channel.save()
                                db_item.channels.add(db_channel)
                        elif 'event_types' == key:
                            for event_type in val['event_type']:
                                try:
                                    db_event_type = models.EventType.objects.get(id=event_type['id'])
                                except:
                                    db_event_type = models.EventType(id=event_type['id'], title=event_type['text'])
                                    db_event_type.save()
                                db_item.event_types.add(db_event_type)
                        elif 'tags' == key:
                            for tag in val['tag']:
                                try:
                                    db_tag = models.Tag.objects.get(name=tag)
                                except:
                                    db_tag = models.Tag(name=tag)
                                    db_tag.save()
                                db_item.tags.add(db_tag)

                        elif 'links' == key:
                            models.Link.objects.filter(material=db_item).delete()
                            if isinstance(val['link'], list):
                                for link in val['link']:
                                    add_link(db_item, link)
                            else:
                                add_link(db_item, val['link'])

                        # TODO: subjects
                        # TODO: geographic_areas
                        # TODO: contact_peoples
                        # TODO: related_items
                        # TODO: instant_messaging
                        # TODO: comments
            except:
                report['errors'] += 1

    return report
