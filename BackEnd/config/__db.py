from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

def configure_mysql(app):
    app.config['MYSQL_DATABASE_HOST'] = os.getenv("BD_HOST")
    app.config['MYSQL_DATABASE_USER'] = os.getenv("BD_USER")
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("BD_PASSWORD")
    app.config['MYSQL_DATABASE_DB'] = os.getenv("BD_TABLE")

    mysql = MySQL()
    mysql.init_app(app)
    
    return mysql