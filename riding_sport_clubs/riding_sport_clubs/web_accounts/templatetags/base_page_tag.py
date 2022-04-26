from django import template

from riding_sport_clubs.web_accounts.models import Profile

register = template.Library()


@register.simple_tag
def has_user(request):
    n = Profile.objects
    return

