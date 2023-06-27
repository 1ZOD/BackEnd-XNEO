from flaskext.mysql import MySQL

def configure_mysql(app):
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # substitua pelo host do seu banco de dados
    app.config['MYSQL_DATABASE_USER'] = 'root'  # substitua pelo nome de usuário do seu banco de dados
    app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'  # substitua pela senha do seu banco de dados
    app.config['MYSQL_DATABASE_DB'] = 'Tarefas'  # substitua pelo nome do seu banco de dados

    mysql = MySQL()
    mysql.init_app(app)
    
    return mysql