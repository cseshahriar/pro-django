import logging

from django.contrib import admin
from django.urls import path

logger = logging.getLogger(__name__)
logger.debug('------------ Project urls.py loaded')
logger.info('------------ Project urls.py loaded')
logger.warning('------------ Project urls.py loaded')
logger.error('------------ Project urls.py loaded')

urlpatterns = [
    path('admin/', admin.site.urls),
]
