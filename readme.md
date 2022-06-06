## Quickstart

Run uvicorn app.app.main:app --reload from the root folder.

Your .env file will need to be in the root folder and this will automatically populate the `settings` object in app.app.core.config.

## Database

All database setup files are stored in the /db folder. Here you will find a more detailed readme.

## Github Actions

In the `.github` folder we can specify workflows which we want to take place in github on specific actions.

In the `actions.yml` file there is an action specified to run pytest when a commit is pushed to the repo. Environment variables relating to tests are specified in this yml file.

It will be necessary to provide a database and associated environment variables in order for any tests relating to databases to pass.

## Get env vars

Update the app name in the makefile file for the development version of your app. Then in order to download your env vars, run `make get_env`.

## Shell

Since there is no built-in shell for Fast API, one has been set up. Running `make shell` from the root folder of the project will run the `manage.py` file in interactive mode, which is the same experience as Flask Shell. You can make additional variables, such as the database session, available by default in shell sessions by initializing them in the `manage.py` file.
