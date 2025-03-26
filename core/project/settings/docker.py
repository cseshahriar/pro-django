if IN_DOCKER:  # noqa
    print('------ running in Docker mode ....')
    assert MIDDLEWARE[:1] == [  # noqa
        'django.middleware.security.SecurityMiddleware',
    ]
