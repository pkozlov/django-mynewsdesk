from django.db import models

# Material types

TYPE_PRESSRELEASE = 'pressrelease'
TYPE_NEWS = 'news'
TYPE_BLOG_POST = 'blog_post'
TYPE_EVENT = 'event'
TYPE_IMAGE = 'image'
TYPE_VIDEO = 'video'
TYPE_DOCUMENT = 'document'
TYPE_CONTACT_PERSON = 'contact_person'

SUBSCRIBE_ENDINGS = {
    TYPE_PRESSRELEASE: 'pressreleases',
    TYPE_NEWS: 'news',
    TYPE_BLOG_POST: 'blog_posts',
    TYPE_EVENT: 'events',
    TYPE_IMAGE: 'images',
    TYPE_VIDEO: 'videos',
    TYPE_DOCUMENT: 'documents',
    TYPE_CONTACT_PERSON: 'contact_person'
}

class Tag(models.Model):
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=255, primary_key=True)
    level = models.IntegerField(blank=True, null=True)

# class Pressroom(models.Model):
#     id = models.IntegerField(primary_key=True)
#     country = models.CharField(max_length=255, blank=True, null=True)
#     country_code = models.CharField(max_length=3, blank=True, null=True)
#     source_name = models.CharField(max_length=255, blank=True, null=True)
#     source_id = models.CharField(max_length=255, blank=True, null=True)
#     header = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     address_street = models.TextField(blank=True, null=True)
#     address_postal_code = models.TextField(blank=True, null=True)
#     address_city = models.TextField(blank=True, null=True)
#     address_country = models.TextField(blank=True, null=True)
#
#     tag_cloud = models.ManyToManyField(Tag)

# class Logotype(models.Model):
#     pressroom = models.ForeignKey(Pressroom, related_name='logotypes')
#     size = models.CharField(max_length=50, blank=True, null=True)
#     image = models.URLField()

class Channel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

# class Subject(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     parent_id = models.CharField(max_length=255, null=True)
#     name = models.TextField()

# class GeographicArea(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     parent_id = models.CharField(max_length=255, null=True)
#     name = models.TextField()

class EventType(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.TextField()

class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=15)
    language = models.CharField(max_length=10)

    channels = models.ManyToManyField(Channel, related_name='materials', blank=True, null=True)

    source_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    pressroom_name = models.CharField(max_length=255, blank=True, null=True)
    pressroom_id = models.IntegerField(blank=True, null=True)
    pressroom = models.CharField(max_length=10, blank=True, null=True)
    organization_number = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    published_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    header = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    boilerplate = models.TextField(blank=True, null=True)

    # for contact person

    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    specialist = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone_alternative = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pressroom_contact = models.NullBooleanField(blank=True, null=True)

    # for event

    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    signup_url = models.URLField(blank=True, null=True)
    event_types = models.ManyToManyField(EventType, related_name='materials', blank=True, null=True)

    # for image
    photographer = models.TextField(blank=True, null=True)
    image_format = models.CharField(max_length=10, blank=True, null=True)
    image_size = models.BigIntegerField(blank=True, null=True)
    image_dimensions = models.CharField(max_length=50, blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)

    # for video
    flash_video = models.URLField(blank=True, null=True)
    flash_video_width = models.IntegerField(blank=True, null=True)
    flash_video_height = models.IntegerField(blank=True, null=True)
    embed_code = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)

    # for document
    document_format = models.CharField(max_length=10, blank=True, null=True)
    document_size = models.BigIntegerField(blank=True, null=True)
    document = models.URLField(blank=True, null=True)

    image = models.URLField(blank=True, null=True)
    image_thumbnail_large = models.URLField(blank=True, null=True)
    image_thumbnail_medium = models.URLField(blank=True, null=True)
    image_thumbnail_small = models.URLField(blank=True, null=True)

    attached_pdf = models.URLField(blank=True, null=True)
    attached_doc = models.URLField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='materials', blank=True, null=True)
    # subjects = models.ManyToManyField(Subject, related_name='materials', blank=True, null=True)
    # geographic_areas = models.ManyToManyField(GeographicArea, related_name='materials', blank=True, null=True)

    # contact_people = models.ManyToManyField('self', blank=True, null=True)
    # related_items = models.ManyToManyField('self', blank=True, null=True)

# class InstantMessaging(models.Model):
#     material = models.ForeignKey(Material, related_name='instant_messaging')
#     type = models.CharField(max_length=255)
#     text = models.TextField()
#
# class Comment(models.Model):
#     material = models.ForeignKey(Material, related_name='comments')
#     author_url = models.URLField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     text = models.TextField(blank=True, null=True)

class Link(models.Model):
    material = models.ForeignKey(Material, related_name='links')
    url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
