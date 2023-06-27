from flask import Flask
from config.db import configure_mysql

app = Flask(__name__)
mysql = configure_mysql(app)


@app.route('/')
def hello():
    return 'Olá, mundo!'



@app.route('/teste')
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    cursor.close()
    # Faça algo com os dados obtidos
    return 'Exemplo de conexão com o MySQL usando o Flask'



if __name__ == '__main__':
    app.run()