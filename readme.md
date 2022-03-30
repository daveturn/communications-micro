## Quickstart

Run uvicorn app.app.main:app --reload from the root folder.

Your .env file will need to be in the root folder and this will automatically populate the `settings` object in app.app.core.config.

## Database

You must make sure that your test and production databases contain a schema called 'freshdesk'.

## Github Actions

In the `.github` folder we can specify workflows which we want to take place in github on specific actions.

In the `actions.yml` file there is an action specified to run pytest when a commit is pushed to the repo. Environment variables relating to tests are specified in this yml file.

It will be necessary to provide a database and associated environment variables in order for any tests relating to databases to pass.
