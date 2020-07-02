from django import template
from reviews.models import Review
register = template.Library()


@register.simple_tag
def get_rating(user):
    r = Review.objects.avg_rating(user)
    if r is not None:
        return r
    else:
        return 0

@register.simple_tag
def total_review(user):
    a = Review.objects.filter(doctor=user).count()
    return a