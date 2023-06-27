from flask import Flask, jsonify
from service.insert.insert_service import Insert
from config.__db import configure_mysql

app = Flask(__name__)
mysql = configure_mysql(app)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Pagina nao encontrada'}), 404


@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({'error': 'Ocorreu um erro durante o processamento da solicitação'}), 500


@app.route('/')
def home():
    return 'Back End Rodando!'


@app.route('/teste')
def index():
    try:
        data = Insert(mysql).get_All()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
