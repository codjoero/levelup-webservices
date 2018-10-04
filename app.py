from flask import Flask, jsonify, request, abort, make_response
from tasks import Tasks
from accounts import Accounts

app = Flask(__name__)

account = Accounts()
task = Tasks()

""" 
Error Handlers 
"""
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)

""" 
Accounts Endpoits
"""
@app.route('/todo/api/v0.1/users', methods=['POST'])
def create_user():
    return jsonify({'New User': account.create_user()}), 201


@app.route('/todo/api/v0.1/users', methods=['GET'])
def get_users():
    return jsonify({'Users': account.accounts}), 201


@app.route('/todo/api/v0.1/users/login', methods=['PATCH'])
def login_user():
    return jsonify({'Status': account.login_user()}), 200


@app.route('/todo/api/v0.1/users/<string:username>', methods=['GET'])
def logout_user(username):
    return jsonify({'Status': account.logout_user(username)}), 201


@app.route('/todo/api/v0.1/users/<int:task_id>', methods=['DELETE'])
def delete_user():
    return jsonify({'Status': account.delete_user()}), 201

""" 
Tasks Endpoints
"""
@app.route('/todo/api/v0.1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task.show_all()})


@app.route('/todo/api/v0.1/tasks', methods=['POST'])
def create_task():
    return jsonify({'task': task.create_task()}), 201


@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['PUT'])
def mark_finished(task_id):
    return jsonify({'task': task.mark_finished(task_id)})


@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return jsonify({'result': task.delete_task(task_id)})


@app.route('/todo/api/v0.1/tasks/deleted/<int:task_id>', methods=['POST'])
def undelete_task(task_id):
    return jsonify({'result': task.undelete_task(task_id)}), 201


@app.route('/todo/api/v0.1/tasks/del/all', methods=['DELETE'])
def delete_all():
    return jsonify({'result': task.delete_all()})


if __name__ == '__main__':
    app.run(debug=True)