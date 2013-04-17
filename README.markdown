# IP based authentication for Django #

To install add the middleware to `MIDDLEWARE_CLASSES`:

    'django_ip_authn.authentication.Middleware',

You also need to add the authentication backend to `AUTHENTICATION_BACKENDS`. This will probably not already exist, in which case you will want the entirety of this:

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'django_ip_authn.authentication.Authenticate',
    )

By default it will not authenticate until you also add in the IP numbers that it should allow:

    VALID_IP_NUMBERS = [
        '127.0.0.1', '127.0.1.1', # Allow only localhost IP numbers
    ]

Currently it will automatically allow the user with ID 1, this is the user that you create during the initial database creation in Django.

There is an optional header to determine which `request.META` header value to use to get the remote IP number. This defaults to `REMOTE_ADDR`. If you are behind a HTTP router you may need to set this to something like the X-Forwarded-For:

    REMOTE_IP_HEADER='HTTP_X_FORWARDED_FOR'

Make sure that your HTTP router always sets this or you will open the possibility for a remote client to get around the IP number check by just setting a header on the request.

