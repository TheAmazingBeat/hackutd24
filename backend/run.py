from routes.server import create_app
from flask import redirect, url_for

app = create_app()

if __name__ == "__main__":
    app.run(debug = True)