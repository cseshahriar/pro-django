if IN_DOCKER:  # type: ignore  # noqa
    print('------ running in Docker mode ....')
    assert MIDDLEWARE[:1] == [   # type: ignore # noqa
        'django.middleware.security.SecurityMiddleware',
    ]
