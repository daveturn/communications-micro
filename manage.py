from IPython import embed

from app.app.main import app  # where your fastAPI app is located, you can initialize it here

@app.command()
def runserver():
    app()


@app.command()
def shell():
    embed()