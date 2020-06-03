from django.utils.text import slugify
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

import os

def order_id():
    return os.urandom(3).hex()


def unique_user_id_generator(instance):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    new_user_id = random_string_generator().upper()
 
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(user_unique_id=new_user_id).exists()
    if qs_exists:
        return unique_user_id_generator(instance)
    return new_user_id

def unique_appointment_id_generator(instance):
    new_appointment_id = random_string_generator().upper()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(appointment_id=new_appointment_id).exists()
    if qs_exists:
        return unique_appointment_id_generator(instance)
    return new_appointment_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug