import celery
import os
from datetime import timedelta


from . import celeryconfig

import logging

logger = logging.getLogger(__name__)


celery_app = celery.Celery(__name__)
celery_app.config_from_object(celeryconfig)

@celery_app.task(name="update_tickets")
def update_tickets():
    import asyncio
    from app.app.freshdesk.tasks import UpdateFreshdeskDataTask
    from app.app.db.init_db import get_session, DatabaseName
    from app.app.freshdesk.client import FreshdeskClient
    from app.app.core.config import settings

    freshdesk = FreshdeskClient(
        api_key=settings.FRESHDESK_API_KEY,
        domain=settings.FRESHDESK_DOMAIN_NAME,
        version=settings.FRESHDESK_API_VERSION
    )

    get_datawarehouse_session = get_session(DatabaseName.DATAWAREHOUSE)
    get_read_only_prod_session = get_session(DatabaseName.TURN_READ_ONLY_PROD)

    logger.info('celery task update_tickets')
    task = UpdateFreshdeskDataTask(
        datawarehouse_session=next(get_datawarehouse_session()),
        read_only_prod_session=next(get_read_only_prod_session()),
        freshdesk=freshdesk

    )
    
    asyncio.run(task.run())


celery_app.conf.beat_schedule = {
    "update_tickets": {
        "task": "update_tickets",
        "schedule": timedelta(minutes=15)
    }
}

