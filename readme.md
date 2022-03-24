## Quickstart

Run uvicorn app.app.main:app --reload from the root folder.

Your .env file will need to be in the root folder and this will automatically populate the `settings` object in app.app.core.config.

## Database

You must make sure that your test and production databases contain a schema called 'freshdesk'.
