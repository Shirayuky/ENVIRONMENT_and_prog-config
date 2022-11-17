import os
from flask import Flask
import dotenv

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
dotenv.load_dotenv(override=True)

@app.route('/')
def environment_page():
    if os.environ.get('APP_CONFIG') == 'development':
        # то указываем путь
        app.config.from_pyfile('config/development.py')
        title = app.config.get('TITLE')
        description = app.config.get('DESCRIPTION')
        return f"<p>{title} - {description}</p>"
    else:
        app.config.from_pyfile('config/production.py')
        title = app.config.get('TITLE')
        description = app.config.get('DESCRIPTION')
        return f"<p>{title} - {description}</p>"


app.run()