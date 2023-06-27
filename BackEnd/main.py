from flask import Flask, jsonify, request
from service.insert.insert_service import Insert
from service.select.select_service import Select
from service.delete.delete_service import Delete
from service.update.update_service import Update
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
    return 'BackEnd Rodando!'


@app.route('/listar-tarefas', methods=['GET'])
def list():
    try:
        data = Select(mysql).getAll()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/registrar-tarefa', methods=['POST'])
def register():
    try:
        body = request.get_json()
        task_content = body['task_content'] 
        Insert(mysql).post_task(task_content)
        return jsonify("OK"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        body = request.get_json()
        id = body['id'] 
        Delete(mysql).delete(id)
        return jsonify("OK"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        body = request.get_json()
        task_content = body['task_content']

        Update(mysql).update(id, task_content)
        return jsonify("OK"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
