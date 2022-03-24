web: uvicorn app.app.main:app --host 0.0.0.0 --port $PORT
beat: celery -A worker.celery_app worker --beat -l info