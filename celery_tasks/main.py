from celery import Celery
from datetime import timedelta


from . import celeryconfig

import logging

logger = logging.getLogger(__name__)


celery_app = Celery(__name__)
celery_app.config_from_object(celeryconfig)


@celery_app.task(name="example_task")
def example_task():
    pass


celery_app.conf.beat_schedule = {
    "example_task": {
        "task": "example_task",
        "schedule": timedelta(days=1),
    }
}
