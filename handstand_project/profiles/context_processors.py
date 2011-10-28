from django.conf import settings
from django.utils.functional import lazy, memoize, SimpleLazyObject

from profiles.utils import get_profile

def lazy_profile(request):
    """
    Returns context variables required by templates that assume a profile
    on each request
    """

    def get_user_profile():
        if hasattr(request,'my_profile'):
            return request.my_profile
        else:
            return get_profile()

    data = {
        'my_profile': SimpleLazyObject(get_user_profile),
        }
    return data
