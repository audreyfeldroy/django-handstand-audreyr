from profiles.models import Profile

def get_profile(user):
    
    """ Rather than throw an error on get_profile, we just return None.
        Makes handling of anonymous users in non-loggedin areas easier.
    """
    if user.is_anonymous():
        return None

    try:
        return user.get_profile()
    except Profile.DoesNotExist:
        return None