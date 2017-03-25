from django.contrib.auth.models import AnonymousUser

def profile_from_request(request):
    """
    Get the profile of the user in the request, or None if not logged in
    :param request: Http request
    :return: request.user's Profile or None
    """
    if isinstance(request.user, AnonymousUser):
        return None
    else:
        return request.user.user_profile


def pkgen(length):
    from base64 import b32encode
    from hashlib import sha1
    from random import random
    rude = ('fuck', 'shit', 'damn', 'bitch', 'hell',)
    bad_pk = True
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:length]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk