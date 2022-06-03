import os

broker_url = os.environ["REDIS_URL"]
result_backend = os.environ["REDIS_URL"]

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = True
