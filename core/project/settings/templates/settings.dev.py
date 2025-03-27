SECRET_KEY = 'django-insecure-6lkd-cvq$gu3r&%^atqhy-o_rmrm(1afh(zk2-a86w*r2_vdwd'
DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore  # noqa
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['cooking_core']['level'] = 'DEBUG'  # type: ignore # noqa
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore # noqa
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore # noqa
