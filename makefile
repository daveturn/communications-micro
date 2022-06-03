get_env:
	heroku config -s -a [DEV_APP_NAME_HERE] > .env

shell:
	python3 -i manage.py